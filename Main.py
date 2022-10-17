import imp


import time
from tracemalloc import start
start_time = time.time()

print("Hello")
a = 10
# ini
#  komentar
print(a) #komen

"""""komen multiple line
baris banyak"""

print(time.time() - start_time, "detik")
# kita fdapat mengkompile python ke kode
# yang namanya bytecoe
# cara compile buka terminal adn pakai yang lain
# python -m py_compile [nama file python]