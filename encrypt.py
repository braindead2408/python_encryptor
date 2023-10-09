#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def generate_key():
	return Fernet.generate_key()

def save_key(key, filename):
	with open(filename, 'wb') as key_file:
		key_file.write(key)
		
def load_key(filename):
	with open(filename, 'rb') as key_file:
		return key_file.read()
	
def encrypt_file(key, input_filename, output_filename):
	fernet = Fernet(key)
	with open(input_filename, 'rb') as file:
		file_data = file.read()
	encrypted_data = fernet.encrypt(file_data)
	with open(output_filename, 'wb') as encrypted_file:
		encrypted_file.write(encrypted_data)
		
def decrypt_file(key, input_filename, output_filename):
	fernet = Fernet(key)
	with open(input_filename, 'rb') as encrypted_file:
		encrypted_data = encrypted_file.read()
	decrypted_data = fernet.decrypt(encrypted_data)
	with open(output_filename, 'wb') as decrypted_file:
		decrypted_file.write(decrypted_data)
		
# Example usage:
if __name__ == "__main__":
	key = generate_key()
	save_key(key, 'encryption_key.key')
	
	input_filename = 'plaintext.txt'
	encrypted_filename = 'encrypted.txt'
	decrypted_filename = 'decrypted.txt'
	
	encrypt_file(key, input_filename, encrypted_filename)
	decrypt_file(key, encrypted_filename, decrypted_filename)
	