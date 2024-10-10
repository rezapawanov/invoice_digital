import csv
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
import qrcode

# Function to load encryption key from a JSON config file
def load_encryption_key(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
        encryption_key = config['encryption_key'].encode('utf-8')  # Convert to bytes
    return encryption_key

# Function to load the plaintext from a CSV file with a single row of data
def load_plaintext_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            plaintext = row[0]  # Since there's only one line in the CSV, take the first entry
            return plaintext

# Function to pad data using PKCS7
def pad_data(data):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

# Function to encrypt data using AES-CBC with a fixed IV
def encrypt_aes_cbc(plain_text, key, iv):
    # Convert plain_text to bytes if it's not already
    if isinstance(plain_text, str):
        plain_text = plain_text.encode('utf-8')

    # Padding the data
    padded_data = pad_data(plain_text)

    # Initialize the AES cipher in CBC mode with the provided fixed IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Encode the encrypted data in base64
    encoded_encrypted_data = base64.b64encode(encrypted_data)

    return encoded_encrypted_data.decode('utf-8')

# Function to generate a QR code from the encrypted message and save with a dynamic name
def create_qr_code(data, identifier, file_name=None):
    if file_name is None:
        file_name = f"QR_{identifier}.png"  # Use identifier to create the file name
    
    # Create a QR code instance with the encrypted message
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size
    )
    qr.add_data(data)  # Add the encrypted message data
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_name)  # Save the image to a file
    print(f"QR code saved as {file_name}")

# Example usage
def main():
    # Load encryption key from config.json file
    encryption_key = load_encryption_key('config.json')  # JSON file storing encryption key

    # Load plaintext from the single-row CSV file
    plaintext = load_plaintext_from_csv('data.csv')  # CSV file storing plaintext

    # Extract identifier (the second part, e.g., 52401845) from the plaintext
    identifier = plaintext.split('|')[1]  # This will extract '52401845'

    # Fixed 16-byte IV (all zeros)
    fixed_iv = bytes([0] * 16)  # 16-byte IV consisting of all zero bytes

    # Encrypt the plaintext using the fixed IV and the key from the config file
    encrypted_message = encrypt_aes_cbc(plaintext, encryption_key, fixed_iv)

    # Output the encrypted message in Base64 format
    print(f"Encrypted Message (Base64): {encrypted_message}")

    # Generate and save the QR code with a dynamic name based on the identifier
    create_qr_code(encrypted_message, identifier)

if __name__ == "__main__":
    main()
