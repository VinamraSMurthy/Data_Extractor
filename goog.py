# importing required libraries
import os, io
import pandas as pd
from google.cloud import vision
from google.cloud import vision_v1
# calling up google vision json file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/Dell/Desktop/Application_Data_Extractor/apikey.json'
# initiate a client
client = vision.ImageAnnotatorClient()
# setting up required path
folder_path = r'C:/Users/Dell/Desktop/Application_Data_Extractor/src/temp'
image_path = 'gray.jpg'
file_path = os.path.join(folder_path,image_path)
# load image into memory
with io.open(file_path,'rb') as image_file:
    file_content = image_file.read()
# perform text detection from the image
image_detail = vision.Image(content=file_content)
response = client.document_text_detection(image=image_detail)
# print text from the dcoment
doctext = response.full_text_annotation.text
print(doctext)