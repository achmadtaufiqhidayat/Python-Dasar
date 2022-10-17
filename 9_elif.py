uang = input("Jumlah uang saya adalah : ")
hutang = 10000

if int(uang) < hutang:
    print("uang tidak cukup")
elif int(uang) == hutang:
    print("Terimakasih, hutang sudah lunas") 
else:
   print("Terimakasih sudah membayar, kembaliannya adalah ", int(uang)-hutang)