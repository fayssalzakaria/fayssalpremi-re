import cv2

#import de l'algorythme
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# lecture de l'image
img = cv2.imread('download.jpg')