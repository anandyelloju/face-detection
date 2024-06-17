import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

def face_det(image):
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    test_image = cv2.imread(image)
    
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor= 1.2, minNeighbors= 5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 0, 255), 2)

    return image_copy
   
if __name__ == '__main__':  
    image = '/home/student/Desktop/FastAPIPro/Test-cases_Images/single_animal.heic'    #'Anand_Yelloju.jpeg'
    detected_image = face_det(image)
    # Display the output
    cv2.imshow('detected_image', detected_image)
    cv2.waitKey()

