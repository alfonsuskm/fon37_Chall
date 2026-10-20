from Crypto.Util.number import getPrime, bytes_to_long
from math import gcd
p = getPrime(512)
q = getPrime(512)
n = p*q
pt = b'REDACTED'
phi = (p-1)*(q-1)

while True:
    d = getPrime(160)
    if gcd(d, phi) == 1:
        e = pow(d, -1, phi)
        break
def rol(val, r, width):
    r %= width
    mask = (1 << width) - 1
    return ((val << r) | (val >> (width - r))) & mask

def ror(val, r, width):
    r %= width
    mask = (1 << width) - 1
    return ((val >> r) | (val << (width - r))) & mask
    
WIDTH = 1024

c = pow(bytes_to_long(pt), e, n)

c = ror(c, 7, WIDTH)
n = rol(n, 3, WIDTH)
e = ror(e, 4, WIDTH)
with open("output.txt", "w") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
