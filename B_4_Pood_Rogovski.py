from poodmodul import *

ostud=[]
hinnad=[]
ostnud=[]
ostnudh=[]

print("Tere!")
pood(ostud,hinnad)
while True:
    #try:
        choice=int(input("0 - vaata ostud ja hinnad\n1 - Koosta tšekk\n2 - Näitab tähestikulises järjekorras\n3 - Leia kõige kallim/odavam kaup\n4 - Leia hind\n5 - Clear nimekirja ja lisa andmed\n6 - exit\n"))
        if choice == 0:
            print(ostud,"\n",hinnad)
        elif choice == 1:
            koostamine(ostud,hinnad,ostnud,ostnudh)
        elif choice == 2:
            sorteerimine(ostud,hinnad)
        elif choice == 3:
            kaloda(ostud,hinnad)
        elif choice == 4:
            hinaleia(ostud,hinnad)
        elif choice == 5:
            tahtleia(ostud,hinnad)
        elif choice == 6:
            break
    #except ValueError:
    #    print("vale andmetüüp!")
