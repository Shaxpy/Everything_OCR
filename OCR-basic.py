from PIL import Image
import pytesseract

im=Image.open("123.jpeg")
text=pytesseract.image_to_string(im,lang='eng')
print(text)