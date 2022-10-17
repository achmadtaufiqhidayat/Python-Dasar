p1 = {"char":"attack titan", "power":300}
p2 = {"char":"armor titan", "power":350}

def train(player):
    player["power"]+=100

def attack(attacker, defernder):
    if(attacker['power'] > defernder['power']):
        print("Serangan berhasil, terus konsisten ", attacker['char'])
    else:
        print("Serangan lemah, terus berjuang ", attacker['char'])

train(p1)
attack(p1,p2)