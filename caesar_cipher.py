#caesar_cipher

print('Positive number indicates left shift\nNegative number indicates right shift')
d=int(input('Enter a number to shift to: '))
msg=input('Enter message: ')
if d<0:
    d=26+d

#Encryption
enc=''
for each in msg:
    a=ord(each)
    if 65<=a<=90: #A-Z
        a+=d
        if a>90:
            a-=26
        enc+=chr(a)
    elif 97<=a<=122: #a-z
        a+=d
        if a>122:
            a-=26
        enc+=chr(a)
    else: #other
        enc+=chr(a)
print('Encrypted text: '+str(enc))

#Decryption
dec=''
for each in enc:
    a=ord(each)
    if 65<=a<=90:
        a-=d
        if a<65:
            a+=26
        dec+=chr(a)
    elif 97<=a<=122:
        a-=d
        if a<97:
            a+=26
        dec+=chr(a)
    else:
        dec+=chr(a)
print('Decrypted text: '+str(dec))
