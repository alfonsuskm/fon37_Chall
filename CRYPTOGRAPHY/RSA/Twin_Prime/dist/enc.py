from Crypto.Util.number import getPrime, bytes_to_long, isPrime
e = 65537
while True:
    p = getPrime(512)
    q = p + 2
    if isPrime(q):
        break
n = p*q
e = 65537
pt = b'REDACTED'

c = pow(bytes_to_long(pt), e, n)

with open("output.txt", "a") as f:
    f.write(f"N = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
