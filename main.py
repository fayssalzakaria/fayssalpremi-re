import cv2

#import de l'algorythme
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# lecture de l'image
img = cv2.imread('images.jpg')

# convertion en niveau de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detection du visage
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#dessin du rectangle autour du visage
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# afficher la cortie
cv2.imshow('img', img)
cv2.waitKey()