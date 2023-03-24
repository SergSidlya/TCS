import docx

def get_text_from_docx_file(file_path):
    try:
        doc = docx.Document(file_path)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    paragraphs_text = []
    for paragraph in doc.paragraphs:
        paragraphs_text.append(paragraph.text)

    return '\n'.join(paragraphs_text)

file_path = "./DockerB.docx"
text = get_text_from_docx_file(file_path)
if text is not None:
    print(text)
