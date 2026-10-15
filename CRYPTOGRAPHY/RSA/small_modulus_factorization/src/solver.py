from Crypto.Util.number import long_to_bytes
from sympy import factorint
N = 8816917104884918891
e = 65537
c = 6061165930721076528

factors = factorint(N)
p, q = factors.keys()

#Bisa juga pakai factordb (skill issue)

#a = isqrt(N)
#if a * a < N:
#    a += 1
#
#while True:
#    b2 = a * a - N
#    b = isqrt(b2)
#
#    if b * b == b2:
#        p = a - b
#        q = a + b
#        break
#
#    a += 1
#
#print("p =", p)
#print("q =", q)

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
pt = pow(c, d, N)
print(long_to_bytes(pt).decode())