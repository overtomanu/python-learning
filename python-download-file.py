import os
import requests
import tempfile
from tqdm import tqdm  # only required to show progress bar

os.chdir(tempfile.gettempdir())

# downloading a file
# pdf_file_url = 'https://pdfobject.com/pdf/sample.pdf'
pdf_file_url = "https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q"
pdf_file_response = requests.get(url=pdf_file_url)

# print byte content
# print("csv_file_response.content => ", pdf_file_response.content)

# write to file, straight forward code
# file_handle = open("sample.pdf", "wb")
# file_handle.write(pdf_file_response.content)

# write to file showing progress


response = requests.get(pdf_file_url, stream=True)

with open("sample-1.pdf", "wb") as file_handle2:
    for data in tqdm(response.iter_content()):
        file_handle2.write(data)