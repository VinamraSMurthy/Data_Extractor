import PyPDF2
import os, io
import pandas as pd
from pdf2image import convert_from_path
from google.cloud import vision
from google.cloud import vision_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/Dell/Desktop/Application_Data_Extractor/apikey.json'
# initiate a client
client = vision.ImageAnnotatorClient()

def extract_data(filename):
    with io.open(filename,'rb') as image_file:
        file_content = image_file.read()
# perform text detection from the image
        image_detail = vision.Image(content=file_content)
        response = client.document_text_detection(image=image_detail)
# print text from the dcoment
        doctext = response.full_text_annotation.text
        print(doctext)
    

filenames=['page0.jpg','page1.jpg','page2.jpg','page3.jpg']
def extract_page_from_pdf(filename):
    images = convert_from_path(filename)
 
    for i in range(len(images)):
   
      # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        
    #print(filenames)
    for page in filenames:
        extract_data(page)
    
extract_page_from_pdf("example-new.pdf")
    