from math import prod
from sympy import factorint
from Crypto.Util.number import long_to_bytes

N = 26737652784447824816384428086856501625569311134337483933863833143705155684381
e = 65537
c = 8749805725856537902597823750019213303047913181322899096702267221346662892384


primes = list(factorint(N))        # empat prima
phi = prod(p - 1 for p in primes)  # phi(n) = (p-1)(q-1)(r-1)(s-1)
d = pow(e, -1, phi)
m = pow(c, d, N)

print(long_to_bytes(m).decode())