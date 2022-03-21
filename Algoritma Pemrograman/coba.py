
from numpy import append


batas = int(input("masukkan batas angka N:\n"))

sum = 0
listAngka = []
for i in range(1, batas+1):
    if (i % 5) == 0:
        sum += i
        listAngka.append(i)
    if (i < 5):
        sum = 0
    else:
        "Input tidak diketahui"

print(f'Angka kelipatan 5:\n{listAngka}')
print(f'Hasil penjumlahan :\n{sum}')
