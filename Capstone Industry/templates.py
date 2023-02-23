#This class is for storing information gained from the images in an orderly fashion.

class BoundingBox:
    def __init__(self, key, value, left, top, indiWidth, indiHeight):
        self.left = left
        self.top = top
        self.key = key
        self.value = value
        self.indiWidth = indiWidth
        self.indiHeight=indiHeight


class Template:

    def __init__(self, name, boxes):
        self.boxes = boxes
        self.name = name


def calibrateMedi(left, top, width, height):
    boxes = []
    #this list takes in the left coord of the document, the top, the width and the height of the doc and calculates the
    #position of the top left corners of the key word bounding boxes.
    boxes.append(BoundingBox("memberNumber", "value", left+(width*0.204), top+(height*0.331), width*0.78, height*0.1))
    boxes.append(BoundingBox("refNum", "value", left+(width*0.052), top+(height*0.479), width*.028, height*.06))
    boxes.append(BoundingBox("name", "value", left+(width*0.11), top+(height*0.4808), width*0.89, height*0.06))
    boxes.append(BoundingBox("valid to", "value", left+(width*0.658), top+(height*0.868), width*0.168, height*0.048))
    return boxes

#Licence
def calibrateWALic(left, top, width, height):
    boxes = []
    #this list takes in the left coord of the document, the top, the width and the height of the doc and calculates the
    #position of the top left corners of the key word bounding boxes.
    boxes.append(BoundingBox("Surname", "value", left+(width*0), top+(height*0.38), width*0.3, height*0.05))
    boxes.append(BoundingBox("Name", "value", left+(width*0), top+(height*0.43), width*.46, height*.06))
    boxes.append(BoundingBox("Address", "value", left+(width*0), top+(height*0.44), width*0.46, height*0.06))
    boxes.append(BoundingBox("City", "value", left+(width*0), top+(height*0.5), width*0.5, height*0.1))
    boxes.append(BoundingBox("Expiry", "value", left+(width * 0.033), top+(height * 0.66), width * 0.25, height * 0.05))
    boxes.append(BoundingBox("DOB", "value", left+(width * 0.333), top+(height * 0.66), width*.3, height*.05))
    boxes.append(BoundingBox("LicenceNum", "value", left+(width * 0.8), top+(height * 0.29), width * 0.165, height*.05))
    return boxes



def calibratePassport(left, top, width, height):
    boxes = []
    #this list takes in the left coord of the document, the top, the width and the height of the doc and calculates the
    #position of the top left corners of the key word bounding boxes.
    boxes.append(BoundingBox("Surname", "value", left+(width*0.3), top+(height*0.22), width*0.4, height*0.06))
    boxes.append(BoundingBox("Name", "value", left+(width*0.3), top+(height*0.27), width*0.4, height*.06))
    boxes.append(BoundingBox("Nationality", "value", left+(width*0.3), top+(height*0.35), width*0.3, height*0.04))
    boxes.append(BoundingBox("DOB", "value", left+(width*0.3), top+(height*0.41), width*0.3, height*0.06))
    boxes.append(BoundingBox("Sex", "value", left+(width * 0.3), top+(height * 0.47), width * 0.1, height * 0.06))
    boxes.append(BoundingBox("DOI", "value", left+(width * 0.3), top+(height * 0.56), width*.24, height*.06))
    boxes.append(BoundingBox("Expiry", "value", left+(width * 0.3), top+(height * 0.62), width * 0.24, height*.06))
    boxes.append(BoundingBox("Authority", "value", left + (width * 0.3), top + (height * 0.718), width * 0.24, height * 0.06))
    boxes.append(BoundingBox("Place of Birth", "value", left + (width * 0.677), top + (height * 0.4), width * .25, height * .2))
    boxes.append(BoundingBox("PassportNo", "value", left + (width * 0.7), top + (height * 0.14), width * 0.2, height * .1))
    return boxes


