from Crypto.Util.number import getPrime, bytes_to_long
p, q, r, s = getPrime(64), getPrime(64), getPrime(64), getPrime(64)
n = p*q*r*s
e = 65537
pt = b'PR1MANYA_K0K_BAN4YAKK!!!!'

c = pow(bytes_to_long(pt), e, n)

with open("output.txt", "w") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")

