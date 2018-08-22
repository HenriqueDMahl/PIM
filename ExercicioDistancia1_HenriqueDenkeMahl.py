import cv2
import numpy
import random
from random import randrange

img = cv2.imread('/home/udesc/Downloads/imagens/lena.jpg',0)

def ruido(img,n):
    h, w = img.shape
    escolhas = [0,255]
    while(n > 0):
        x = randrange(h)
        y = randrange(w)
        p_b = random.choice(escolhas)
        if img[y,x] != p_b:
            print "Trocou de {} para {}".format(img[y,x],p_b)
            img[y,x] = p_b
            n -= 1

    cv2.imshow('ruido', img)
    cv2.imwrite("ruido.jpg",img)
    cv2.waitKey(0)

ruido(img,500)
