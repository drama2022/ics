'''NEEDS PYCRYPTODOME, METHOD MENTIONED IN AES.PY'''
 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
 
keyPair = RSA.generate(3072)
 
pubKey = keyPair.publickey()
print(f"Public key :  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
 
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

#ENCRYPTION
msg = input('Enter a message for encryption : ')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted : ", binascii.hexlify(encrypted)) 

# DECRYPTION
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted Message is : " , decrypted)