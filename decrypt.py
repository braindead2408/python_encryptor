#!/usr/bin/env python3

from cryptography.fernet import Fernet

def load_key():
	with open('encryption_key.key', 'rb') as key_file:
		return key_file.read()
	
def decrypt_file(key, input_filename, output_filename):
	fernet = Fernet(key)
	with open(input_filename, 'rb') as encrypted_file:
		encrypted_data = encrypted_file.read()
	decrypted_data = fernet.decrypt(encrypted_data)
	with open(output_filename, 'wb') as decrypted_file:
		decrypted_file.write(decrypted_data)
		
if __name__ == "__main__":
	key = load_key()
	encrypted_filename = 'static/encrypted_files/encrypted_file.txt'
	decrypted_filename = 'plaintext_files/decrypted_file.txt'
	
	decrypt_file(key, encrypted_filename, decrypted_filename)
	