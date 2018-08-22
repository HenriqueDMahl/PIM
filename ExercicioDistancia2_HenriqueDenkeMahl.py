import cv2
import numpy as np

img = cv2.imread('E:\\Trabalhos\\Trabalhos_UDESC\\PIM\\ruido.jpg',0)

def media(img,n):
    p = n/2
    img = cv2.copyMakeBorder(img, top=p, bottom=p, left=p, right=p, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
    h, w = img.shape


    for i in range(p,h-p):
        for j in range(p,w-p):
            media = 0.0
            mascara = img[i-p:i+(p+1),j-p:j+(p+1)]
            for k in mascara:
                for l in k:
                    media += l
            media = media/(n*n)
            img[i,j] = media
            #print img[i-p:i+(p+1),j-p:j+(p+1)]

    resultado = img[p:h-p,p:w-p]

    cv2.imshow('media', resultado)
    cv2.imwrite("media.jpg",resultado)
    cv2.waitKey(0)


media(img,5)
