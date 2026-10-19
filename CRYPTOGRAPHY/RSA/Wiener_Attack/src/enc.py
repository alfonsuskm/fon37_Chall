from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = 65537
pt = b'the_WI3NERSSS_takes_1t_ALL'
phi = (p-1)*(q-1)

while True:
    d = getPrime(160)
    if gcd(d, phi) == 1:
        e = pow(d, -1, phi)
        break

c = pow(bytes_to_long(pt), e, n)
ptx = pow(c, d, n)
with open("output.txt", "w") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
