import docx
import os

file_path = os.path.join(os.getcwd(), 'Docker Basics.docx')

document = docx.Document(file_path)

for paragraph in document.paragraphs:
    print(paragraph.text)
