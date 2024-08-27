import os
import random

coloured_circles = {
  "piros": '🔴',
  "kek": '🔵',
  "zold": '🟢',
  "sarga": '🟡',
  "narancs": '🟠',
  "lila": '🟣',
  "fekete": '⚫',
  "feher": '⚪',
  "barna": '🟤'
}
#https://www.sigmoid.hu/index.php?action=termekszinozon
lista = []
jatek_vege = True
eletek = 11
tippek = []

for _ in range(4):
  lista.append(random.choice(list(coloured_circles.keys())))

#Megjelenites
display = []
for _ in range(len(lista)):
  display += "?"

#Bekeres
while jatek_vege:
  for i in range(4):
    print(f"Add meg az {i+1} színt")
    tipp = input("Egy szint kerek: ").lower()
    tippek.append(tipp)
    # tipp = input("Spaceval elválasztva adj meg 4 szint ").lower().split()

    os.system('cls')


    #Megnezzuk, a talalt szin pontosan hol helyezkedik el, majd megjelenitjuk
    for position in range(len(lista)):
        szin = lista[position]
        if szin == tipp:
            display[position] = szin
    # #Megnezzuk, hogy van-e meg el nem talalt szin, ha nincs akkor jatek vege
    if "?" not in display:
      jatek_vege = False
      

    print("  ".join(display))
    print(tippek)

print("Nyertel!")
