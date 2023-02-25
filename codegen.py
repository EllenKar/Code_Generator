print("----------------------------")
print("CODE GENERATOR")
print("----------------------------")
print("Make your password more secure with encryption!")
print()
encrypt_cod = input("Please put down a text password, no caps.")
#the below creates two variables that substitute a letter for another, and back.
def encryptious(encrypt_cod):
    encrypted = encrypt_cod.maketrans("abcdefghijklmnopqrstuvwxyz", "wvutsrqponmlkjihgfedcbazyx")
    crypt_ed = encrypt_cod.translate(encrypted)
    return crypt_ed

print(encryptious(encrypt_cod))
print()
decrypt_cod = input("Please input your encrypted password to decrypt it.")
#the below does the opposite, to decrypt the encrypted.
def decryptious(decrypt_cod):
    decrypted = decrypt_cod.maketrans("wvutsrqponmlkjihgfedcbazyx", "abcdefghijklmnopqrstuvwxyz")
    crypt_de = decrypt_cod.translate(decrypted)
    return crypt_de

print(encryptious(decrypt_cod))
