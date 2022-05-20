''' Before executing the script it is necessary to install crypto library named as PYCRYPTODOME. To install it :
Open Terminal and run -: pip install pycryptodome'''

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
password = input("Enter Password : ")
print("The Password is :", password)

hash_obj = SHA256.new(password.encode('utf-8'))
hkey = hash_obj.digest()
#print("Message Digest : ", hkey, len(hkey))

def encrypt (info):
    msg = info
    BLOCK_SIZE = 16
    PAD = "{"
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PAD
    cipher = AES.new(hkey, AES.MODE_ECB)
    result = cipher.encrypt(padding(msg).encode('utf-8'))
    return result

msg = input('Enter message to be encrpted : ')
ciphertext = encrypt(msg)
print("The Encrypted Text is : ", ciphertext)

def decrypt(info):
    msg = info
    PAD = "{"
    decipher = AES.new(hkey, AES.MODE_ECB)
    pt = decipher.decrypt(msg).decode('utf-8')
    pad_index = pt.find(PAD)
    result = pt[:pad_index]
    return result

plaintext = decrypt(ciphertext)
print("Your Original text is :" , plaintext)
