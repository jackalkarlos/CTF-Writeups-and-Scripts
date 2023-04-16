from z3 import *
import re
from pwn import *


def convertbaba(islem):
    eq_parts = islem.split('=')
    lhs = eval(eq_parts[0].strip())
    rhs = int(eq_parts[1].strip())
    eq = lhs == rhs
    return eq

r = remote("0.cloud.chals.io",23434)
islem = r.recv().decode('utf-8')
print(islem)
satirlar = islem.split("\n")
ilk_islem = satirlar[1]
ikinci_islem = satirlar[2]
ucuncu_islem = satirlar[3]

#filtering

desen = r"\b[-\d*()]+|\w+|\S+"
ilk_islem_clean = re.findall(desen, ilk_islem)
ilk_islem_clean[2] = "x)"
ilk_islem_clean[6] = "y)"
ilk_islem_clean[10] = "z)"


ilk_islem_clean = " ".join(ilk_islem_clean)

ikinci_islem_clean = re.findall(desen, ikinci_islem)
ikinci_islem_clean[2] = "x)"
ikinci_islem_clean[6] = "y)"
ikinci_islem_clean[10] = "z)"


ikinci_islem_clean = " ".join(ikinci_islem_clean)

ucuncu_islem_clean = re.findall(desen, ucuncu_islem)
ucuncu_islem_clean[2] = "x)"
ucuncu_islem_clean[6] = "y)"
ucuncu_islem_clean[10] = "z)"
ucuncu_islem_clean = " ".join(ucuncu_islem_clean)

solver = Solver()

x = Int('x')
y = Int('y')
z = Int('z')


solver.add(convertbaba(ilk_islem_clean))
solver.add(convertbaba(ikinci_islem_clean))
solver.add(convertbaba(ucuncu_islem_clean))

# Solver'ı çöz
if solver.check() == sat:
    model = solver.model()
    x_val = model[x].as_long()
    y_val = model[y].as_long()
    z_val = model[z].as_long()
else:
    print("Denklemler çözülemedi.")

print(x_val)
print(y_val)
print(z_val)

x_val = str(x_val)
r.sendline(x_val)
time.sleep(1)
y_val = str(y_val)
r.sendline(y_val)
time.sleep(1)
z_val = str(z_val).encode()
r.sendline(z_val)
print(r.recv())
print(r.recv())
print(r.recv())



