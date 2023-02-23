import templates
import mediDetect
import LicenceDetect
import passportDetect


def main():
    #takes in an image and a document type and returns the dictionary of key value pairs from the image
    dictionary= process("connork.png", "passport")
    print(dictionary)

#executes the correct extraction fundtion based on the document type passed in
def process(img, docType):
    if docType == 'passport':
        boxes = templates.calibratePassport(0, 0, 1, 1)
        bucket = 'testextraction'
        photo = img
        dictionary = passportDetect.detectText(photo, bucket, boxes)


    elif docType=='licence':
        boxes = templates.calibrateWALic(0, 0, 1, 1)
        bucket = 'testextraction'
        photo = img
        dictionary = LicenceDetect.detectText(photo, bucket, boxes)


    elif docType == 'medicare':
        boxes = templates.calibrateMedi(0, 0, 1, 1)
        bucket = 'testextraction'
        photo = img
        dictionary = mediDetect.detectText(photo, bucket, boxes)

    return dictionary







if __name__ == '__main__':
    main()