"""tidak boleh duplikat,
ga ada indeks
tidak berurutan 
jarang dipakai"""

angka = {1,2,5,3,6,6,7,3}
angka2 = {1,3,4,7,5,3,2,2,3,4,5}

print("Himpunan 1 : ", angka)
print("Himpunan 2 : ", angka2)
print(angka2 | angka)
print(angka & angka2)
print(angka2 - angka)
print(angka ^ angka2)