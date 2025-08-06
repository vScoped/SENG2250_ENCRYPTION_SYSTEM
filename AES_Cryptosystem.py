from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time
import random

# *** PART A *** 
AES_KEY_HEX = 'c3478362a4b1e7d9c8f23b6e09d4782fbb45e1d09a7c12d3fe89a5c4b6d3f271'
PLAINTEXT_HEX = '476f6c64656e2073616e64207761726d732074686520666565742c2077617665732063726173682067656e746c792c20736561626972647320676c6964652061626f76652e'

# create an flag to check validity of hex - could be found in a library

# *** PART B *** 
timestamp = hex(int(time.time()))[2:] # timestamp component represents the last 10 bits (in hex format) and guarantees uniqueness
IV_128_HEX = '325cd072752c7fd95b3712c5' + str(timestamp)   
print(IV_128_HEX)

# *** PART C *** 

# converting to correct format (bytes)
BLOCK_SIZE = 16 # Bytes
AES_key = bytes.fromhex(AES_KEY_HEX) # 32 Bytes
plaintext = bytes.fromhex(PLAINTEXT_HEX) # 64 Bytes
padded_text = pad(plaintext, BLOCK_SIZE) # padding to be 64 Bytes
IV = bytes.fromhex(IV_128_HEX) # 16 Bytes


# Block Cypher Encryption 
nonce = IV

cipher = AES.new(AES_key, AES.MODE_ECB)

cipher_encryption_block_output = cipher.encrypt(nonce)

decrypted_message = cipher.decrypt(cipher_encryption_block_output)

# Creating cypher text (through XOR) - XOR occurs through binary
x = zip(plaintext, cipher_encryption_block_output)

cipher_message = bytes(a ^ b for a, b in zip(plaintext, cipher_encryption_block_output))[2:]

print(cipher_message.hex())

# TODO - Decryption - hopefully works 🙏

# output - Separating into blocks of decryption
print(f"""
    Entire Plaintext: {str(plaintext)[1:]}
    Key: (represented in HEX) {AES_KEY_HEX}
    IV: (represented in HEX) {IV_128_HEX}
      """)

""" For each block: (size 16) 
    print (Input of AES: XXXX...XXXX
    Output of AES: XXXX...XXXX
    Result of XOR: XXXX...XXXX)

"""

print(f"Entire Ciphertext (represented in HEX): ")
 
# Part D
def bitflip(bit):
    return '1' if bit == '0' else '0'

PLAINTEXT_128_BYTES = b"Color tell story"

# bit-flip occuring 5 times
PLAINTEXT_ARR = []

for i in range(5):
    PLAINTEXT_128_BITS = bin(int.from_bytes(PLAINTEXT_128_BYTES))
    rand_index = random.randint(0, 127)
    flipped_bit = bitflip(PLAINTEXT_128_BITS[rand_index])
    PLAINTEXT_128_BITS = PLAINTEXT_128_BITS[:rand_index] + flipped_bit + PLAINTEXT_128_BITS[rand_index + 1:]
    PLAINTEXT_ARR.append(PLAINTEXT_128_BITS)

# Ciphering each plaintext
cipheredtext_arr = []
for item in PLAINTEXT_ARR:
    item_bytes  = int(item, 2).to_bytes(16) 
    item = cipher.encrypt(item_bytes)
    item = bin(int.from_bytes(item))[2:]

    # formatting into hex
    item_hex =  hex(int(item, 2))[2:]
    cipheredtext_arr.append(item_hex)

# displaying each ciphertext 
for i in range(len(cipheredtext_arr)):
    print(f"Ciphertext {i} = {cipheredtext_arr[i]}")
print("*** Ciphertext is displayed in hexadecimal format to better interpret the results")

# From results it clearly exhibits the avalance effect as Ciphertext is vastly different to each other.