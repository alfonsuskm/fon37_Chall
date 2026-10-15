from Crypto.Util.number import *
from math import gcd
p = getPrime(256)
q = getPrime(256)
n = p*q
e = 65537
e2 = 65539
phi = (p-1)*(q-1)

pt = b'REDACTED'

d = pow(e, -1, phi)
d2 = pow(e2, -1, phi)
c1 = pow(bytes_to_long(pt), e, n)
c2 = pow(bytes_to_long(pt), e2, n)

with open("output.txt", "a") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"e2 = {e2}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"c2 = {c2}\n")

