import numpy as np
import boto3
import process

#generates client to use aws text extraction
def detectText(photo, bucket, boxes):
    client = boto3.client('rekognition', 'ap-southeast-2')
    img = process.getImage(bucket, photo)
    #small amount of processing on the image to improve extraction results
    exposed = process.overExpose(np.array(img), [255, 255, 110])
    byteboi = process.numpy_to_binary(exposed)
    #using filterbyregion text extraction can isolate the areas of the image predetermined to be of interest
    response = client.detect_text(Image={'Bytes': byteboi},
                                      Filters={"WordFilter": {
                                                "MinConfidence": 96},
                                          "RegionsOfInterest":
                                              [
                                                {"BoundingBox":
                                                   {"Width": boxes[0].indiWidth,
                                                    "Height":boxes[0].indiHeight,
                                                    "Left":boxes[0].left,
                                                    "Top":boxes[0].top,}

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

                                                }

                                              ]
                                            }
                                      )

    textDetections = response['TextDetections']

    #This loop isolates the strings of importants and assigns them them correct key.
    #finally the results arte returned as a dictionary
    for text in textDetections:
        if text['Type'] == 'LINE':
            if text['Confidence']>98 and process.isNum(text['DetectedText']):
                if boxes[0].value == 'value':
                    boxes[0].value = text['DetectedText']
            if text['Confidence']>98:
                if boxes[1].value == "value":
                    boxes[1].value = text["DetectedText"][0]
                if boxes[2].value == 'value' and process.isName(text['DetectedText']):
                    boxes[2].value = text['DetectedText'][1:]
            if '/' in text['DetectedText']:
                if boxes[3].value == 'value':
                    boxes[3].value = text['DetectedText']

    dictionary = {
        "Member Number": boxes[0].value,
        "Reference Number": boxes[1].value,
        "Name":boxes[2].value,
        "Valid to":boxes[3].value
    }
    return dictionary








