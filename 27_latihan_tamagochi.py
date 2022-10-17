nameM = input("Nama monster anda? ")
monster = {"name":nameM, "power":100}

def startGame():
    pilih = input("Mau ngapain ? 1. Makan 2. Mandi 3. Keluar Game")
    if pilih == "1":
        goEat()
    elif pilih == "2":
        goBath()
    elif pilih == "3":
        goOut()
    else:
        print("Ulangi dari awal game")
        startGame()

def goEat():
    print("Nyam..nyam..nyam..")
    monster["power"]+= 100
    startGame()

def goBath():
    print("Byur..byur..byur..")
    print(monster['power'], "adalah power saat ini")
    startGame()

def goOut():
    print("Bye..bye..bye.")
    

startGame()