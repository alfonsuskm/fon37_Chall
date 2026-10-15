from Crypto.Util.number import getPrime, bytes_to_long
p = getPrime(32)
q = getPrime(32)
n = p*q
e = 65537
pt = 'REDACTED'
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

c = pow(bytes_to_long(pt), e, n)
ptx = pow(c, d, n)
with open("output.txt", "a") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
