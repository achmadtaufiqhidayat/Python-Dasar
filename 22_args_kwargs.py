#digunakna ketika kita tidak tahu berapa jumlah data yang dimasukkan (dinamis)

#args
def arguments(*name):
   for nama in name:
    print(nama)

arguments('susilo', 'alena', 'alan', 'prima')

#kwargs
def kwarguments(**man):
    for key, value in man.items():
        print (key + " - "+ value)

kwarguments(name = 'hidayat', age='21', hobby = 'sing')