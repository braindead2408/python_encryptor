# File Encryptor

File Encryptor is a simple Python web application that allows users to upload files, encrypt them using the Fernet encryption scheme, and download the encrypted files.

## Installation

Follow these steps to set up and run the File Encryptor:

1. Clone the repository to your local machine:
   ```git clone https://github.com/your-username/file-encryptor.git```
   
**Change into the project directory**:
```cd file-encryptor```

**Install the required Python packages**. You can use pip to install them from the requirements.txt file:
```pip install -r requirements.txt```

Generate the encryption key using the provided Python script:
```python generate_key.py```

This will create an encryption_key.key file in the project directory. Keep this file secure, as it is used for encryption and decryption.

Run the Flask application:
```python app.py```


**The application should now be running at http://localhost:5000.**

Usage

Step 1: Access the File Encryptor web interface in your web browser at http://localhost:5000.

Step 2: Upload a file using the "Select a file to encrypt" input.

Step 3: Click the "Encrypt File" button to encrypt the uploaded file.
You can then download the encrypted file using the "Download Encrypted File" link.

Customization
You can customize the appearance and functionality of the web interface by modifying the index.html file and the associated CSS files (custom.css or others).

**Dependencies**
```Flask: Flask Documentation```
```cryptography: cryptography Documentation```
