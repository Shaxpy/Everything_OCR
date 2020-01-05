from PIL import Image
import pytesseract
import io
from wand.image import Image as wi
pdfImage=wi(filename="2.png",resolution=300)
#if needed to be used as pdf reader---
#pdfImage=pdf.convert("jpeg")
imageBlobs=[]
for img in pdfImage.sequence:
    imgPage=wi(image=img)
    imageBlobs.append(imgPage.make_blob('png'))
recog_text=[]

for imgBlob in imageBlobs:
    im=Image.open(io.BytesIO(imgBlob))
    text=pytesseract.image_to_string(im,lang='eng',config='-c preserve_interword_spaces=1 --oem 1 --psm 6 ')
    text= text.replace('\n','')
    recog_text.append(text)
print(recog_text)
