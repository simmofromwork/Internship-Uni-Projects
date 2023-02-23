import process
import numpy as np
import boto3
import process
import templates
from PIL import Image


#def setUpDetect(photo, bucket, boxes):

    #detectText(img, client, boxes)

def detectText(photo, bucket, boxes):
    client = boto3.client('rekognition', 'ap-southeast-2')
    img = process.getImage(bucket, photo)
    if process.orientate(np.array(img)):
        img = img.rotate(90)
    # small amount of processing on the image to improve extraction results
    byteboi = process.numpy_to_binary(np.array(img))
    # using filterbyregion text extraction can isolate the areas of the image predetermined to be of interest
    dictionary = getText(client, byteboi, boxes)
    #CHECK HOW SUCCESSFUL EXTRACTION WAS TO ASCERTAIN IF UPSIDE DOWN
    if process.valueCount(dictionary) >2:
        img= img.rotate(180)
        byteboi = process.numpy_to_binary(np.array(img))
        dictionary = getText(client, byteboi, templates.calibrateWALic(0,0,1,1))

    return dictionary

def getText(client, byteboi, boxes):
    response = client.detect_text(Image={'Bytes': byteboi},
                                  Filters={"WordFilter": {
                                      "MinConfidence": 95},
                                      "RegionsOfInterest":
                                          [
                                              {"BoundingBox":
                                                   {"Width": boxes[0].indiWidth,
                                                    "Height": boxes[0].indiHeight,
                                                    "Left": boxes[0].left,
                                                    "Top": boxes[0].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[1].indiWidth,
                                                    "Height": boxes[1].indiHeight,
                                                    "Left": boxes[1].left,
                                                    "Top": boxes[1].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[2].indiWidth,
                                                    "Height": boxes[2].indiHeight,
                                                    "Left": boxes[2].left,
                                                    "Top": boxes[2].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[3].indiWidth,
                                                    "Height": boxes[3].indiHeight,
                                                    "Left": boxes[3].left,
                                                    "Top": boxes[3].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[4].indiWidth,
                                                    "Height": boxes[4].indiHeight,
                                                    "Left": boxes[4].left,
                                                    "Top": boxes[4].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[5].indiWidth,
                                                    "Height": boxes[5].indiHeight,
                                                    "Left": boxes[5].left,
                                                    "Top": boxes[5].top, }

                                               },
                                              {"BoundingBox":
                                                   {"Width": boxes[6].indiWidth,
                                                    "Height": boxes[6].indiHeight,
                                                    "Left": boxes[6].left,
                                                    "Top": boxes[6].top, }

                                               }

                                          ]
                                  }
                                  )

    textDetections = response['TextDetections']
    # This loop isolates the strings of importants and assigns them them correct key.
    # finally the results arte returned as a dictionary
    for text in textDetections:
        print(text['DetectedText'])
        if text['Type'] == 'LINE':
            if boxes[6].value == 'value'and process.isNum(text["DetectedText"]):
                boxes[6].value = text['DetectedText']
            elif boxes[0].value == 'value':  # and not process.isNum(text["DetectedText"]):
                boxes[0].value = text['DetectedText']
            elif boxes[1].value == 'value' and not process.isNum(text["DetectedText"]):
                boxes[1].value = text['DetectedText']
            elif boxes[2].value == 'value':
                boxes[2].value = text['DetectedText']
            elif boxes[3].value == 'value':
                boxes[3].value = text['DetectedText']
            elif boxes[4].value == 'value':
                boxes[4].value = text['DetectedText']
            elif boxes[5].value == 'value':
                boxes[5].value = text['DetectedText']
    dictionary = {
        "Licence Number": boxes[6].value,
        "Surname": boxes[0].value,
        "Name": boxes[1].value,
        "Address": boxes[2].value,
        "City": boxes[3].value,
        "Expiry": boxes[4].value,
        "D.O.B": boxes[5].value,
    }
    return dictionary




