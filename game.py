import sys
import time
import os
#print(".", end="\r", flush=True)
#time.sleep(1)
#print("..", end="\r", flush=True)
#time.sleep(1)
#print("...", end="\r", flush=True)
#print("\n")
#print("Countdown done!!!")
#clear = lambda: os.system('cls')
#clear()
#print("Hallo")
class game():
    def __init__ (self):
        self.ü = 1

    def lade(self):
        print("_____________")
        print("| TicTacToe |")
        print("|   V3.0    |")
        print("|_____3_____|", end="\r", flush=True)
        time.sleep(1)
        print("|_____2_____|", end="\r", flush=True)
        time.sleep(1)
        print("|_____1_____|", end="\r", flush=True)
        time.sleep(1)
        print("|_____GO____|")
        clear = lambda: os.system('cls')
        clear()

    def show(self, z1, z2, z3):
        print("_____________")
        print("|   TTT     |")
        print("| " + z1[0] + " | " + z1[1] + " | " + z1[2] + " |")
        print("|___________|")
        print("| " + z2[0] + " | " + z2[1] + " | " + z2[2] + " |")
        print("|___________|")
        print("| " + z3[0] + " | " + z3[1] + " | " + z3[2] + " |")
        print("|___________|")
    def update(self, name, felder):
        e = False
        z = []
        if name == "z1":
            z = [felder[0], felder[1], felder[2]]
        elif name == "z2":
            z = [felder[0], felder[1], felder[2]]
        elif name == "z3":
            z = [felder[0], felder[1], felder[2]]
        elif name == "s1":
            z = [felder[0], felder[3], felder[6]]
        elif name == "s2":
            z = [felder[1], felder[4], felder[7]]
        elif name == "s1":
            z = [felder[2], felder[5], felder[8]]
        else:
            print("Error")
            e = True
        if e == True:
            return(z)

#    def winabfrage(self, z1, z2, z3, s1, s2, s3):




mygame = game()
os.system("color 0B")
mygame.lade()
felder = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
while True:
#   abfrage = mygame.abfrage()
    z1 = mygame.update("z1", felder)
    z2 = mygame.update("z2", felder)
    z3 = mygame.update("z3", felder)
    s1 = mygame.update("s1", felder)
    s2 = mygame.update("s2", felder)
    s3 = mygame.update("s3", felder)
    mygame.show(z1, z2, z3)
#   mygame.winabfrage()
