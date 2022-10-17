def teks():
    print("Ini function tanpa parametet")

teks()

def text2(text):
    print("Ini function dengan parameter", text)

text2("sepi")

def nulable(int = 12):
    print("Ini function dengan parameter default ", int)

nulable()

def kalkulator(a,b):
    print("Penjumlahan ", a+b)
    print("Pengurangan ",a-b)
    print("Pembagian ",a/b)
    print("Perkalian ",a*b)
    print("Modulo ", a%b)

kalkulator(10,3)
