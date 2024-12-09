from flask import Flask, jsonify, send_from_directory, request
from docx import Document
import os

app = Flask(__name__)
FILE_DIRECTORY = "./files"  # Percorso relativo alla cartella files

@app.route('/files', methods=['GET'])
def list_files():
    # Lista i file nella cartella files
    files = [f for f in os.listdir(FILE_DIRECTORY) if f.endswith('.docx') or f.endswith('.pdf')]
    return jsonify(files)

@app.route('/files/<path:filename>', methods=['GET'])
def get_file_content(filename):
    # Percorso del file
    file_path = os.path.join(FILE_DIRECTORY, filename)
    if not os.path.exists(file_path):
        return "File non trovato", 404

    # Legge il contenuto
    if filename.endswith('.docx'):
        doc = Document(file_path)
        content = '\n'.join([p.text for p in doc.paragraphs])
        return content
    elif filename.endswith('.pdf'):
        from PyPDF2 import PdfReader
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            content = ''.join([page.extract_text() for page in reader.pages])
        return content
    else:
        return "Formato non supportato", 400

if __name__ == '__main__':
    app.run(debug=True)
