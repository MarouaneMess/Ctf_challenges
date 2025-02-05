def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            result += char
    return result
    
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def vigenere_decipher(text, key):
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                result += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            result += char
    return result

# Decrypt the flag
encrypted_flag = "ehrfdorbtl{d3w1ry3g_fh3_H4jb_m0_Hhd0ts_mTe_zmvlz3}"
caesar_shift = 13
key = "ZNAHFPEVCG"

caesar_decrypted_key = caesar_decipher(key, caesar_shift)
vigenere_decrypted = vigenere_decipher(encrypted_flag, caesar_decrypted_key)

print("Key : ", caesar_decrypted_key)
print("Decrypted Text:", vigenere_decrypted)