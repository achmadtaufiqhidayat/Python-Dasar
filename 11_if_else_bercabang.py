# putri raja mencari joodh yg baik dan rajin

tamu = input("Tamu yang datang adalah : ")
rajin = True
baik = True
usia = input("Berapa usianya? ")

if baik  & rajin :
    if (tamu == "pria") & (int(usia)<50) & (int(usia)>18):
        print("Ini adalah calon ta'aruf putri Pak Romli")
    elif (int(usia)<18) :
        print("Ini adalah murid ngaji Pak Romli")
    elif (tamu != "pria") & (tamu!="cewek"):
        print("Tamu biasa")
    else :
        print("Ini adalah sahabat putri Pak Romli")
else:
    print("Ini siapa ya?")