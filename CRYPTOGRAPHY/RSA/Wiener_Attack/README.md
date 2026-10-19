# Wiener's Attack

attack ini cara kerjanya menggunakan pecahan berkelanjutan untuk dapetin private eksponen d.

Attack ini dapat dilakukan jika ukuran D kecil yang mana kurang dari
```math
\frac{1}{3}\sqrt[4]{n}
```

Hal ini dapat terjadi jika kita menggunakan public eksponent e yang kecil.

## Wiener's theorem
Wiener's attack pada dasarnya mengikuti teori berikut:
```math
n = pq
```
yang mana
```math
q < p < 2q
```
```math
d < \frac{1}{3}\sqrt[4]{n}
```
Ketika diberikan n dan e dengan syarat
 $ed \equiv 1 \pmod{\phi n}$
attacker dapat merecover d secara efesien.

## Attack
Jika kita diberi public key (n,e), maka dapat dilakukan attack yang merecover d.
1. ubah pecahan $\frac{e}{n}$ menjadi pecahan berkelanjutan
$[a_0; a_1, a_2, \ldots, a_{k-2}, a_{k-1}, a_k]$
2. Lakukan iterasi untuk tiap konvergen dalam pecahan berlanjut:
$\frac{a_0}{1},a_0 + \frac{1}{a_1}, a_0 + \frac{1}{a_1 + \frac{1}{a_2},},\ldots,a_0 +\frac{1}{a_1 + \frac{\cdots}{a_{k-2} + \frac{1}{a_{k-1}}}}$
3. Kemudian cek jika konvergennya $\frac{k}{d}$ dengan melakukan:
- Tentukan numerator menjadi k dan denominator menjadi d
- cek jika d adalah ganjil, jika tidak, lanjut ke konvergen selanjutnya
- cek jika $ed \equiv 1 \pmod{k}$ jika tidak, lanjut ke konvergen selanjutnya
- Tentukan $\phi n = \frac{ed - 1}{k}$ dan akar dari polynomial $x^2 - (n - \phi n + 1)x + n$ 
-Jika akar dari polynomial adalah bilangan integer, maka d sudah ketemu(kalau tidak lanjut ke konvergen selanjutnya)
4. Jika semua konvergen sudah dicoba namun nihil, artinya RSA paramater nya tidak vulnerable ke Wiener's attack.

> Kita dapat menggunakan modul python owiener agar mempermudah hidup

[Library Owiener](https://github.com/orisano/owiener)
```python
#!/usr/bin/env python3
import owiener
from Crypto.Util.number import long_to_bytes

#--------Data--------#

N = <N>
e = <e>
c = <c>

#--------Wiener's attack--------#

d = owiener.attack(e, N)

if d:
    m = pow(c, d, N)
    flag = long_to_bytes(m).decode()
    print(flag)
else:
    print("Wiener's Attack failed.")
```

source:
- https://cryptohack.gitbook.io/cryptobook/untitled/low-private-component-attacks/wieners-attack
- https://en.wikipedia.org/wiki/Continued_fraction
- https://medium.com/@it7th/how-wieners-attack-breaks-rsa-when-you-pick-a-weak-private-key-7113fda6d969