import numpy as np
import cv2

img = cv2.imread('/home/udesc/Downloads/t3.jpg')

def harris(img):

    cv2.imshow('Original',img)

    resultado = img

    gray = cv2.cvtColor(resultado,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    blockSize = 13
    ksize = 29
    k = 0.1

    r = cv2.cornerHarris(gray,blockSize,ksize,k)

    resultado[r>0.01*r.max()]=[0,0,255]

    cv2.imshow('harris', resultado)

    cv2.imwrite('teste.png',resultado)

    cv2.waitKey(0)



harris(img)
