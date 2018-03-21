#rsa

def gcd(a,b):
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
  
p=int(input('Enter p value: '))
q=int(input('Enter q value: '))
n=p*q
phi=(p-1)*(q-1)

#gcd(e,phi)=1
e=1
for i in range(2,100):
    if gcd(i,phi)==1:
        e=i
        break
print('e value: '+str(e))

#(d*e)mod(phi)=1
d=1
for i in range(1,100):
    if (i*e)%phi==1:
        d=i
        break
print('d value: '+str(d))

msg=input('Enter message to be encrypted: ')
#encryption -> (M**e)mod(n)=C
enc=[]
for each in msg:
    a=ord(each)-97
    a**=e
    a%=n
    enc.append(a)

print('Encrypted message: '+str(enc))

#decryption -> (C**d)mod(n)=M
dec=''
for each in enc:
    a=each**d
    a%=n
    dec+=chr(a+97)

print('Decrypted message: '+dec)



