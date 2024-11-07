import os
import pyaes

# Open encrypted file
file_name = 'teste.txt.ransomware'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Descryption key
key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
descrypt_data = aes.descrypt(file_data)

# Remove encrypted file
os.remove(file_name)

# Create a new descrypted file
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(descrypt_data)
new_file.close()
