import PIL
import cv2
import numpy as np
from pytesseract import image_to_string
import pytesseract
#from PIL import image
#instalacion de pyteseract
#Windows: https://medium.com/@marioruizgonzalez.mx/how-install-tesseract-orc-and-pytesseract-on-windows-68f011ad8b9b
#https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror
#Además hay que añadirlo con pip install pytesseract
#Mi ruta del binario: C:\Users\gonzalez.locar20\AppData\Local\Programs\Tesseract-OCR
#Tambien hay que ayadir la ruta de la carpeta tessdata a la variable de entorno TESSDATA_PREFIX

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gonzalez.locar20\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image = cv2.imread('../imagenes/matricula1.jpg')
# Convert image to grayscale and sharpen image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
# Adaptive threshold
# Perform morpholgical operations to clean image
# Invert image
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
result = 255 - close

cv2.imshow('result', result)
cv2.waitKey()

custom_config = r'--oem 3 --psm 6'
# pytesseract.image_to_string(result, config=custom_config)
print(pytesseract.image_to_string(image, config=custom_config))
