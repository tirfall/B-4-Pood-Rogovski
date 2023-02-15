def pood(o:list,h:list):
    """Funktsioon võimaldab tellijal sisestada oma tooted ja hinnad nimekirja. Kui kasutaja on väärtused sisestanud, salvestatakse nimekirjad."""
    while True:
        j = 0
        hile = int(input("Kui palju kaupa sa pead nimekirja sisestama?\n"))
        o.clear()
        h.clear()
        while j != hile:
            toode = input("Sisesta toode: ")
            o.append(toode)
            hind = input("Sisesta hind: ")
            h.append(hind)
            j += 1
        print(o,"\n",h)
        ansfin = str(input("Kas kõik on õige? jah või ei\n"))
        if ansfin == "jah":
            break

def koostamine (o:list,h:list,ostnud:list,ostnudh:list):
    """
     Kustuta nimekirjast ostetud toode ja lisa nimekirja ostnud[] ja koosta tšekk; 
    """
    mitutoode = int(input("Mitu toodet sa ostnud?"))
    j = 0
    while j != mitutoode:
        toode = input("Sisesta toode: ")
        ostnud.append(toode)
        o.remove(toode)
        hind = input("Sisesta hind: ")
        ostnudh.append(hind)
        h.remove(hind)
        j += 1
    print(f"Siin on sinu tšekk:\n{ostnud}\n{ostnudh}")

def sorteerimine(o:list,h:list):
    x = zip(o,h)
    xs = sorted(x, key=lambda tup: tup[0])
    print(xs)

def kaloda(o:list,h:list):
    ans=max(h)
    ind=h.index(ans)
    toode=str(o[ind])
    print(toode,ans)
    ans=min(h)
    ind=h.index(ans)
    toode=str(o[ind])
    print(toode,ans)
    return ans,toode

def hinaleia(o:list,h:list):
    tood=input("sisesta toode:")
    if tood in o:
        n=o.count(tood)
        for j in range (n):
            ind=o.index(tood)
            print(o[ind])
            print(h[ind])

    return o,h

def tahtleia(o:list,h:list):
    answer = int(input("1 - clear\n2 - lisa toode ja hind"))
    if answer == 1:
        o.clear()
        h.clear()
        print(o,"\n",h)
    elif answer == 2:
        toode = input("Sisesta toode: ")
        o.append(toode)
        hind = input("Sisesta hind: ")
        h.append(hind)
        print(o,"\n",h)

    return o,h
