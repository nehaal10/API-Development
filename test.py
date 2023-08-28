import hashlib

# string to be hashed
data = "Hello, world!"

# create a new sha256 hash object
hash_object = hashlib.sha256()

# update the hash object with the bytes of the string
hash_object.update(data.encode())

# get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

print(type(hex_dig))
