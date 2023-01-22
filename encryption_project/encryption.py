"""
This program is based on the Casear Shift cipher that encrypts plaintext by shifting each character by 3
"""

plaintext = input("Plaintext: ")
cipher_text = ""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"

plaintext_pos = 0 

while(plaintext_pos < len(plaintext)):
    plaintext_char = plaintext[plaintext_pos]
    alphabet_pos = 3
    while(plaintext_char != alphabet[alphabet_pos]):
        alphabet_pos += 1
    alphabet_pos = alphabet_pos - 3
    cipher_text += alphabet[alphabet_pos]
    plaintext_pos = plaintext_pos + 1

print(cipher_text)
