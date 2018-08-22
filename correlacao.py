import cv2
import numpy as np

img = cv2.imread('/home/udesc/Downloads/imagens/lenasalepimenta.png',0)

def m1(img,n,kernel):
    p = n/2
    h, w = img.shape
    
    resultado = np.zeros(img.shape, np.uint8)
    resultado = img

    resultado = cv2.copyMakeBorder(resultado, top=p, bottom=p, left=p, right=p, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
    
    for i in range(p,h-p):
        for j in range(p,w-p):
            mascara = img[i-p:i+(p+1),j-p:j+(p+1)]
            media = 0.0
            soma = 0.0
            row = 0
            for k in mascara:
            	col = 0
                for l in k:
                	soma += l*kernel[row,col]
                	media += kernel[row,col]
            		col += 1
    		row += 1
    		if soma < 0:
    			soma = 0
    		if soma > 255:
    			soma = 255
            resultado[i,j] = soma
            #print img[i-p:i+(p+1),j-p:j+(p+1)]

    resultado = resultado[p:h-p,p:w-p]
    return resultado

def mascaras(img,n,m):

	div = 0.0
	for i in m:
		for j in i:
			div += j
	if div != 0.0:
		m = m/div
	
	img2 = cv2.filter2D(img,-1,m)
	
	r1 = m1(img,n,m)
	cv2.imshow('Filter2D',img2)
	cv2.imshow('Original',img)
	cv2.imshow('Mascara1', r1)
	cv2.imwrite("maior.jpg",r1)
	cv2.waitKey(0)


m = np.asarray([[1,1,1],[1,1,-2],[1,-2,-2]],dtype = np.float32)
mascaras(img,3,m)
