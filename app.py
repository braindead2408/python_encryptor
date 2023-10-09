from flask import Flask, render_template, request, send_from_directory
from cryptography.fernet import Fernet

app = Flask(__name__)

def load_key():
    with open('encryption_key.key', 'rb') as key_file:
        return key_file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key = load_key()
    fernet = Fernet(key)

    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

        with open('static/encrypted_files/encrypted_file.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        return "File encrypted successfully"

@app.route('/download')
def download():
    return send_from_directory('static/encrypted_files', 'encrypted_file.txt')

if __name__ == '__main__':
    app.run(debug=True)
