import random

def play():
    user = input("taş? kağıt? makas?\n ")
    computer = random.choice(["taş", "kağıt", "makas"])
    print("Bilgisayarın seçimi ^-^ " + computer)
    if user == computer:
        return "Berabere -_- "
    if isWin(user,computer):
        return "Kazandın \o/ "
    
    return "Kaybettin =_=' "

def isWin(player, computer):
    if(player == "taş" and computer == "makas") or (player == "makas" and computer == "kağıt") or  (player == "kağıt" and computer == "taş"):
        return True

print(play())