#substitution_cipher

msg=input('Enter message: ')

#Encryption
enc=''
for each in msg:
    a=ord(each)
    if 65<=a<=77: #A-M
        enc+=chr(a+13)
    elif 78<=a<=90: #N-Z
        enc+=chr(a-13)
    elif 97<=a<=109: #a-m
        enc+=chr(a+13)
    elif 110<=a<=122: #n-z
        enc+=chr(a-13)
    else:
        enc+=chr(a)
print('Encrypted text: '+str(enc))

#Decryption
dec=''
for each in enc: #same code as above
    a=ord(each)
    if 65<=a<=77:
        dec+=chr(a+13)
    elif 78<=a<=90:
        dec+=chr(a-13)
    elif 97<=a<=109:
        dec+=chr(a+13)
    elif 110<=a<=122:
        dec+=chr(a-13)
    else:
        dec+=chr(a)
print('Decrypted text: '+str(dec))

