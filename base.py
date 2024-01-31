import base64

def base64_encrypt(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encrypted_text = encoded_bytes.decode('utf-8')
    return encrypted_text

def base64_decrypt(encrypted_text):
    decoded_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
    decrypted_text = decoded_bytes.decode('utf-8')
    return decrypted_text

text = "Szyfrowanie listy nr3"
encrypted_text = base64_encrypt(text)
print("Zaszyfrowany tekst:", encrypted_text)

# = base64_decrypt(encrypted_text)
#print("Odszyfrowany tekst:", decrypted_text)
