import boto3
import io
import cv2 as cv
import numpy as np
from PIL import Image



def isNum(text):
    result=False
    modText = text
    modText=modText.replace(" ","")
    if not modText.isalpha():
        result = True
    return result

def isName(line):
    result = True
    temp = line
    temp = temp.replace(" ","")
    if not temp[0].isalpha():
        for element in range(1, len(temp)):
            if not temp[element].isalpha():
                result = False
    return result



def numpy_to_binary(arr):
    is_success, buffer = cv.imencode(".jpg", arr)
    io_buf = io.BytesIO(buffer)
    return io_buf.read()


#isolates black pixels in medicare card to improve extraction
def overExpose(card, intensity):
    img = card
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array(intensity)
    mask = cv.inRange(hsv, lower, upper)
    mask_inv = cv.bitwise_not(mask)
    #cv.imshow("ye", mask_inv)
    #cv.waitKey(0)
    return mask_inv


#retreives the specified image from a specified s3 bucket so that it can be manipulated if needed.
def getImage(bucket, photo):
    s3 = boto3.resource('s3', region_name='ap-southeast-2')
    bucket = s3.Bucket(bucket)
    object = bucket.Object(photo)
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)
    return img

def orientate(img):
    yes = False
    imgarray = img.shape
    if imgarray[0]>imgarray[1]:
        yes=True
    return yes

def valueCount(dictionary):
    count = 0
    for x in dictionary.values():
        if x == "value":
            count = count+1
    return count
