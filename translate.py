import os
import io
import re
from google.cloud import translate_v2 as translate
from google.cloud import storage
from google.oauth2 import service_account
from PyPDF2 import PdfFileReader, PdfFileWriter

# Replace the values below with your own Google Cloud project credentials and settings
credentials = service_account.Credentials.from_service_account_file('C:\Users\Taher Farg\3D Objects\Translate\\taher.json')
project_id = 'your-project-id'
storage_bucket = 'your-storage-bucket'

def translate_pdf_to_arabic(pdf_path):
    # Initialize Google Cloud API client
    client = translate.Client(credentials=credentials)

    # Read PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()

        # Extract text from PDF pages
        text = ''
        for page in range(num_pages):
            page_text = pdf_reader.getPage(page).extractText()
            text += page_text

        # Remove non-Arabic characters
        arabic_pattern = re.compile(r'[^\u0621-\u063A\u0641-\u064A\s]+')
        text = arabic_pattern.sub('', text)

        # Translate text to Arabic
        translated_text = client.translate(text, target_language='ar')['translatedText']

        # Write translated text to a new PDF file
        pdf_writer = PdfFileWriter()
        for page in range(num_pages):
            page_text = translated_text[page*num_chars_per_page:(page+1)*num_chars_per_page]
            pdf_writer.addPage(pdf_reader.getPage(page))
            pdf_writer.addBookmark('Page {}'.format(page+1), page)
            pdf_writer.addBookmark('Translated Page {}'.format(page+1), page+num_pages)
            pdf_writer.addBookmark('Original Page {}'.format(page+1), page+2*num_pages)
            pdf_writer.addBookmark('Translated Text', page+3*num_pages)
            pdf_writer.addBookmark('Original Text', page+4*num_pages)
            pdf_writer.addBookmark('Translated Text Page {}'.format(page+1), page+5*num_pages)
            pdf_writer.addBookmark('Original Text Page {}'.format(page+1), page+6*num_pages)
            pdf_writer.addBookmark('End of Page {}'.format(page+1), page+7*num_pages)
            pdf_writer.addBookmark('End of Translated Page {}'.format(page+1), page+8*num_pages)
            pdf_writer.addBookmark('End of Original Page {}'.format(page+1), page+9*num_pages)

        # Save translated PDF file to Google Cloud Storage
        translated_pdf_file_name = os.path.basename(pdf_path).replace('.pdf', '_translated.pdf')
        translated_pdf_file_path = os.path.join('/tmp', translated_pdf_file_name)
        with open(translated_pdf_file_path, 'wb') as pdf_file:
            pdf_writer.write(pdf_file)
        storage_client = storage.Client(project=project_id, credentials=credentials)
        bucket = storage_client.bucket(storage_bucket)
        blob = bucket.blob(translated_pdf_file_name)
        blob.upload_from_filename(translated_pdf_file_path)
        os.remove(translated_pdf_file_path)

    print('Translation complete. Translated PDF saved to {}'.format(translated_pdf_file_name))

# Example usage
pdf_path = 'Lab 4.pdf'
translate_pdf_to_arabic(pdf_path)
