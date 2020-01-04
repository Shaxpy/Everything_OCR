from PIL import Image
import pytesseract
import io
from wand.image import Image as wi
pdf=wi(filename="qqq.pdf",resolution=300)
pdfImage=pdf.convert("jpeg")
imageBlobs=[]
for img in pdfImage.sequence:
    imgPage=wi(image=img)
    imageBlobs.append(imgPage.make_blob('jpeg'))
recog_text=[]

for imgBlob in imageBlobs:
    im=Image.open(io.BytesIO(imgBlob))
    text=pytesseract.image_to_string(im,lang='eng',config='-c preserve_interword_spaces=1')
    recog_text.append(text)
print(recog_text)