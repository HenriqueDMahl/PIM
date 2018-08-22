import cv2
import numpy as np

#Autores: Henrique Denke Mahl, Alexandre M. Fava

img = cv2.imread('/home/udesc/Downloads/harris_car.png')

img2 = cv2.imread('/home/udesc/Downloads/quadrado.png')

def alexandre(img):
    p = 3/2
    h, w, fodase = img.shape

    resultado = np.zeros(img.shape, np.uint8)
    resultado = img

    resultado = cv2.copyMakeBorder(resultado, top=p, bottom=p, left=p, right=p, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
    print
    for i in range(p,h-p):
        for j in range(p,w-p):
                if img[i, j, 2] >= 140 and img[i, j, 1] == img[i, j, 0] == 0:    # dois e vermelho
                    for x in range(50):
                        for y in range (50):
                            print i
                            if j+y<w-p :#DIREITA
                                if (img[i, j+y, 2] == 0 and img[i, j+y, 1] == 0 and img[i, j+y, 0] == 0):
                                    img[i,j+y, 2] = 0
                                    img[i, j+y, 1] = img[i, j+y, 0] = 255
                            if i-x>h-p :#CIMA
                                if (img[i-x, j, 2] == 0 and img[i-x, j, 1] == 0 and img[i-x, j, 0] == 0):
                                    img[i-x,j, 2] = 0
                                    img[i-x, j, 1] = img[i-x, j, 0] = 255
                            if j-y>w-p :#ESQUERDA
                                if (img[i, j-y, 2] == 0 and img[i, j-y, 1] == 0 and img[i, j-y, 0] == 0):
                                    img[i,j-y, 2] = 0
                                    img[i, j-y, 1] = img[i, j-y, 0] = 255
                            if i+x<h-p :#BAIXO
                                if (img[i+x, j, 2] == 0 and img[i+x, j, 1] == 0 and img[i+x, j, 0] == 0):
                                    img[i+x,j, 2] = 0
                                    img[i+x, j, 1] = img[i+x, j, 0] = 255
                            if j+y<w-p and  i-x>h-p :#DIAGONAL DIREITA CIMA
                                if (img[i-x, j+y, 2] == 0 and img[i-x, j+y, 1] == 0 and img[i-x, j+y, 0] == 0):
                                    img[i-x,j+y, 2] = 0
                                    img[i-x, j+y, 1] = img[i-x, j+y, 0] = 255
                            if j+y<w-p and  i+x<h-p :#DIAGONAL DIREITA BAIXO
                                if (img[i+x, j+y, 2] == 0 and img[i+x, j+y, 1] == 0 and img[i+x, j+y, 0] == 0):
                                    img[i+x,j+y, 2] = 0
                                    img[i+x, j+y, 1] = img[i+x, j+y, 0] = 255
                            if j-y>w-p and  i-x>h-p :#DIAGONAL ESQUERDA CIMA
                                if (img[i-x, j-y, 2] == 0 and img[i-x, j-y, 1] == 0 and img[i-x, j-y, 0] == 0):
                                    img[i-x,j-y, 2] = 0
                                    img[i-x, j-y, 1] = img[i-x, j-y, 0] = 255
                            if j-y>w-p and  i+x<h-p :#DIAGONAL ESQUERDA BAIXO
                                if (img[i+x, j-y, 2] == 0 and img[i+x, j-y, 1] == 0 and img[i+x, j-y, 0] == 0):
                                    img[i+x,j-y, 2] = 0
                                    img[i+x, j-y, 1] = img[i+x, j-y, 0] = 255
                            '''if j+y<w-p and i+x<h-p:
                                    if img[i, j-y, 2] == 0 and img[i, j, 1] == 0 and img[i, j, 0] == 0:
                                        img[i-x,j+y, 2] = 0
                                        img[i-x, j+y, 1] = img[i-x, j+y, 0] = 255
                                        if i+x<h-p:
                                            img[i+x, j+y, 1] = img[i+x, j+y, 0] = 255
                                            if j-y<w-p:
                                                img[i-x, j-y, 1] = img[i-x, j-y, 0] = 255'''


                    '''for x in range(20):
                        for y in range (20):
                            #if i-x>=0 and j+y<w-p and j+x<h-p:
                                #img[i-x,j+y, 2] = 0
                                #img[i-x, j+y, 1] = img[i-x, j+y, 0] = 255
                                #continue
                            #else:
                            if i+x<h-p and j-y<w-p:
                                img[i+x,j-y, 2] = 0
                                img[i+x, j-y, 1] = img[i-x, j-y, 0] = 255'''
            #print img[i-p:i+(p+1),j-p:j+(p+1)]

    #resultado = resultado[p:h-p,p:w-p]
    return img



r3 = alexandre(img)
cv2.imshow('TrabFinal', r3)
cv2.imwrite('TrabFinal.png',r3)
cv2.waitKey(0)
