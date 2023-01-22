"""
This program decryptys a Caesar shift cipher text that has a shift value of 3
"""

ciphertext = input("Ciphertext: ")
plaintext= ""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"

ciphertext_pos = 0 

while(ciphertext_pos < len(ciphertext)):
    ciphertext_char = ciphertext[ciphertext_pos]
    alphabet_pos = 3
    while(ciphertext_char != alphabet[alphabet_pos]):
        alphabet_pos = alphabet_pos - 1
    alphabet_pos = alphabet_pos + 3
    plaintext += alphabet[alphabet_pos]
    ciphertext_pos = ciphertext_pos + 1

print(plaintext)
