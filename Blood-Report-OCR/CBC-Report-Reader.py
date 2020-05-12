!pip install pytesseract
!sudo apt install tesseract-ocr
# Gooogle COLAB
import cv2
import pytesseract
import pandas as pd
import numpy as np
# If using Windows---
# pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('.jpg')

text = pytesseract.image_to_string(img)

text = text.split('\n')
df = pd.DataFrame(text)
uncleaned_medical = df[4:].reset_index(drop=True)
uncleaned_medical[0].replace('',np.nan,inplace=True)
cleaned_medical=uncleaned_medical.dropna()

cleaned_medical.columns=['medical_report']

a=[]

for x in cleaned_medical['medical_report']:
    a.append(x.split())
clean_data = pd.DataFrame(a)
clean_data
