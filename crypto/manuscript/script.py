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

def vigenere_cipher(text, key):
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result

# Original key and flag
vigenere_key = "MANUSCRIPT"
flag = "shellmates{d3c1ph3r_th3_P4st_t0_Unl0ck_tHe_futur3}"

# Encrypt the key with Caesar cipher
caesar_shift = 13
caesar_encrypted_key = caesar_cipher(vigenere_key, caesar_shift)

# Encrypt the flag with Vigenère cipher using the encrypted key
vigenere_encrypted_flag = vigenere_cipher(flag, vigenere_key)

print("Encrypted Key:", caesar_encrypted_key)
print("Encrypted Flag:", vigenere_encrypted_flag)