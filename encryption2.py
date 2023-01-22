"""
This program is an improved Caesar Shift cipher that 
extends the range of characters that can be respresented by using ASCII character
"""

plaintext = input("Plaintext: ")
ciphertext = ""
plaintext_pos = 0

while(plaintext_pos < len(plaintext)):
    plaintext_char = plaintext[plaintext_pos]
    ASCII_val = ord(plaintext_char)
    ASCII_val -= 3
    ciphertext += chr(ASCII_val)
    plaintext_pos += 1

print(ciphertext)