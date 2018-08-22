# -*- coding: utf-8 -*-
import cv2
import numpy as np

def conexo(img, terceiro, i, j, numeracao2, indice2):
    if img[i,j]==255 and terceiro[indice2]==0:
        terceiro[indice2] = numeracao2
        conexo(img, terceiro, i, j+1, numeracao2, indice2+1)
        conexo(img, terceiro, i+1, j, numeracao2, indice2+comprimento)
        conexo(img, terceiro, i+1, j+1, numeracao2, indice2+comprimento+1)
        conexo(img, terceiro, i+1, j-1, numeracao2, indice2+comprimento-1)
        
        conexo(img, terceiro, i, j-1, numeracao2, indice2-1)

    return 


img = cv2.imread('/home/udesc/Downloads/imagens/componentes.png',0)
resultado = np.zeros(img.shape, np.uint8)
resultado = img
altura, comprimento = img.shape
terceiro = []

for i in range (0, altura):
    for j in range (0, comprimento):
        terceiro.append(0)

numeracao = 0
indice = 0

for i in range (0, altura): 
    for j in range (0, comprimento):
        if img[i,j]==255 and terceiro[indice]==0:
            numeracao = numeracao + 1
            conexo(img, terceiro, i, j, numeracao, indice)
        indice = indice + 1
            

print "A quantidade de componetes eh ", numeracao

indice = 0
for i in range (0, altura): 
    for j in range (0, comprimento):
        for k in range (1, numeracao+1):
            if terceiro[indice]==k:
                resultado[i,j]=35*k
        indice=indice+1
        
  


cv2.imshow('Filtro', resultado)
cv2.imwrite("resultado.jpg",resultado)
cv2.waitKey(0)
