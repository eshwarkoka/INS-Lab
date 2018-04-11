import numpy as np
from numpy.linalg import inv
data = input('Enter data without space: ')
key = np.array([[2,3],[5,7]])

# pad data if not even
if len(data)%2 != 0:
	data += 'x' # pad byte

# convert data to ascii
plain = []
for each in data:
	plain.append(ord(each)-97)

# consider 2 elements at a time and encrypt
cipher = []
for i in range(0,len(plain),2):
	elements = np.array([plain[i],plain[i+1]])
	encrypted = key.dot(elements)%26
	cipher.append(chr(encrypted[0]+97))
	cipher.append(chr(encrypted[1]+97))

print("Encrypted text: ")
print(''.join(cipher)) #convert list to string

data = cipher

# inverse the key
invkey = inv(key).astype('int') # converting to int since inv will return float

# convert cipher text to numbers
cipher = []
for each in data:
	cipher.append(ord(each)-97)

#consider two elements at a time and decrypt
plain = []
for i in range(0,len(cipher),2):
	elements = np.array([cipher[i],cipher[i+1]])
	decrypted = invkey.dot(elements)%26
	plain.append(chr(decrypted[0]+97))
	plain.append(chr(decrypted[1]+97))

print('Decrypted text: ')
print(''.join(plain))
