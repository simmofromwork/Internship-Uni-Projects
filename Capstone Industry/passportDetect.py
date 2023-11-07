import process
import numpy as np
import boto3
from PIL import Image, ImageDraw, ExifTags, ImageColor
from PIL import Image
import cv2 as cv

def detectText(photo, bucket, boxes):
    client = boto3.client('rekognition', 'ap-southeast-2')
    img = process.getImage(bucket, photo)
    if process.orientate(np.array(img)):
        img = img.rotate(90)
    # small amount of processing on the image to improve extraction results
    #exposed=process.overExpose(np.array(img), [255, 255, 140])
    #cv.imshow("exp", exposed)
    #cv.waitKey(0)
    byteboi = process.numpy_to_binary(np.array(img))
    # using filterbyregion text extraction can isolate the areas of the image predetermined to be of interest
    dictionary = getText(client, byteboi, boxes, img)
    # CHECK HOW SUCCESSFUL EXTRACTION WAS TO ASCERTAIN IF UPSIDE DOWN
    #if process.valueCount(dictionary) > 3:
        #img = img.rotate(180)
        #print("rotated180")
       # byteboi = process.numpy_to_binary(np.array(img))
        ##dictionary = getText(client, byteboi, templates.calibratePassport(0, 0, 1, 1))

    return dictionary


def getText(client, byteboi, boxes, img):
    response = client.detect_text(Image={'Bytes': byteboi},
                                      Filters={"WordFilter": {
                                                "MinConfidence": 98},
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

                                                },
                                                  {"BoundingBox":
                                                       {"Width": boxes[7].indiWidth,
                                                        "Height": boxes[7].indiHeight,
                                                        "Left": boxes[7].left,
                                                        "Top": boxes[7].top, }

                                                   },
                                                  {"BoundingBox":
                                                       {"Width": boxes[8].indiWidth,
                                                        "Height": boxes[8].indiHeight,
                                                        "Left": boxes[8].left,
                                                        "Top": boxes[8].top, }

                                                   },
                                                  {"BoundingBox":
                                                       {"Width": boxes[9].indiWidth,
                                                        "Height": boxes[9].indiHeight,
                                                        "Left": boxes[9].left,
                                                        "Top": boxes[9].top, }
                                                  }]
                                            }
                                      )

    textDetections = response['TextDetections']
    # This loop isolates the strings of importants and assigns them them correct key.
    # finally the results arte returned as a dictionary
    for text in textDetections:
        if text['Type'] == 'LINE':
            print(text['DetectedText'])
            if boxes[9].value == 'value':
                boxes[9].value = text['DetectedText']
            elif boxes[0].value == 'value':
                boxes[0].value = text['DetectedText']
            elif boxes[1].value == 'value':
                boxes[1].value = text['DetectedText']
            elif boxes[2].value == 'value' and text['DetectedText']=="AUSTRALIAN":
                boxes[2].value = text['DetectedText']
            elif boxes[3].value == 'value':
                boxes[3].value = text['DetectedText']
            elif boxes[4].value == 'value' and len(text["DetectedText"]) == 1:
                boxes[4].value = text['DetectedText']
            elif boxes[8].value == 'value':
                boxes[8].value = text['DetectedText']
            elif boxes[5].value == 'value':
                boxes[5].value = text['DetectedText']
            elif boxes[6].value == 'value':
                boxes[6].value = text['DetectedText']
            elif boxes[7].value == 'value':
                boxes[7].value = text['DetectedText']




    passport = {
        "Passport Number": boxes[9].value,
        "Surname": boxes[0].value,
        "Name": boxes[1].value,
        "Nationality": boxes[2].value,
        "D.O.B": boxes[3].value,
        "SEX": boxes[4].value,
        "Date of Issue": boxes[5].value,
        "Date of Expiry": boxes[6].value,
        "Authority":boxes[7].value,
        "Place of Birth":boxes[8].value,
    }

    imgWidth, imgHeight = img.size
    draw = ImageDraw.Draw(img)

    for detectedText in response("")

    box = text['BoundingBox']
    left = imgWidth * box['Left']
    top = imgHeight * box['Top']
    width = imgWidth * box['Width']
    height = imgHeight * box['Height']

    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(width))
    print('Face Height: ' + "{0:.0f}".format(height))

    points = (
        (left, top),
        (left + width, top),
        (left + width, top + height),
        (left, top + height),
        (left, top)

    )
    draw.line(points, fill='#00d400', width=2)

    # Alternatively can draw rectangle. However you can't set line width.
    # draw.rectangle([left,top, left + width, top + height], outline='#00d400')


    img.show()

    return passport
