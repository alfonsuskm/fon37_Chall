flag = b"CMO{IamLokiofAsgardandIamburdenedwithgloriouspurpose}"
secret = b"I_kN0w_Wh4T_K1nD_0F_g0d_I_Need_TO_B3e"
enc = []
def ror(val, r):

    return (
        ((val >> r) | (val << (8-r)))
        & 0xff
    )
for i in range(len(flag)):
    enc1 = flag[i] ^ secret[i % len(secret)]
    enc2 = ror(enc1, 5)
    enc.append(enc2)

print("enc = [" + ", ".join(f"0x{x:02x}" for x in enc) + "]")
print(len(enc))
print(len(secret))