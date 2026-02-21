import random

encrypted_hex = "cb35d9a7d9f18b3cfc4ce8b852edfaa2e83dcd4fb44a35909ff3395a2656e1756f3b505bf53b949335ceec1b70e0"
encrypted_bytes = bytes.fromhex(encrypted_hex)

random.seed(1337)

flag_chars = []
for i in range(len(encrypted_bytes)):
    key_byte = random.randint(0, 255)
    plain_char = encrypted_bytes[i] ^ key_byte
    flag_chars.append(chr(plain_char))

flag = ''.join(flag_chars)
print(flag)