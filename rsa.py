import math
print("Enter two prime numbers")
p = int(input("Enter p: "))
q = int(input("Enter q: "))
n= p*q
msg = int(input("Enter message data = "))
phi=(p-1)*(q-1)
e=2
while msg>n:
print("Message data should be less than modulus(n) ")
msg = int(input("Enter message data = "))


print("Modulus n(p*q) = ",n)

print("Totient function(phi) = ",phi)

while e<phi:
 if math.gcd(e,phi)==1:
    break
 else:
    e += 1

d=0;
while d<(phi):

 if (e*d)%phi==1:
    break
 else:
  d += 1

c = math.pow(msg,e)
c = math.fmod(c,n)
print("Message after encryption = ",c)
m = math.pow(c, d)
m = math.fmod(m, n)
print("Original message sent =  ",m)



