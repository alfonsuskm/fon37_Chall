from Crypto.Util.number import getPrime, bytes_to_long
p1, q1, p2, q2, p3, q3 = getPrime(256), getPrime(256), getPrime(256), getPrime(256), getPrime(256), getPrime(256)
n1 = p1*q1
n2 = p2*q2
n3 = p3*q3

e = 3
pt = b'H4sTAD_BRODCESTT_P4K3_CRT_CEESS'
m = bytes_to_long(pt)

ns = [n1, n2, n3]
cs = [pow(m, e, n) for n in ns]

with open("output.txt", "w") as f:
    for i in range(3):
        f.write(f"N{i+1} = {ns[i]}\n")
        f.write(f"e = {e}\n")
        f.write(f"c{i+1} = {cs[i]}\n")
        f.write("\n")

