"""
This program is an improved decryption Caesar Shift cipher that 
extends the range of characters that can be respresented by using ASCII character
"""

cipher_text = input("Ciphertext: ")
plaintext = ""
cipher_text_pos = 0

while(cipher_text_pos < len(cipher_text)):
    cipher_text_char = cipher_text[cipher_text_pos]
    ASCII_val = ord(cipher_text_char)
    ASCII_val += 3
    plaintext += chr(ASCII_val)
    cipher_text_pos += 1

print(plaintext)