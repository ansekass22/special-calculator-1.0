'''
 Funktio, joka tarkistaa, onko sille annettu luku alkuluku edellisten
 alkulukujen perusteella, tulostaa vastauksen, edelliset alkuluvut
 sekä niiden määrän.
'''
def onko_alkuluku(k,alkuluvut):
    on_alkuluku = True
    i = 0
    while alkuluvut[i] <= k**0.5:
	    if (k % alkuluvut[i]) == 0:
		    on_alkuluku = False
		    break
	    else:
		    i = i + 1
    return on_alkuluku

def alkulukuTulokset(luku):
#print("Tervetuloa alkulukulaskuriin.")
#try:
#luku = float(input("Anna luku: "))
#luku = float(str_luku)
    Alkuluvut = []
    if luku < 2:
        tulos = str(luku) + " ei ole alkuluku; pi(" + str(luku) + ")=0; edell. alkuluvut: " + str(Alkuluvut)
    elif luku == 2:
        tulos = "2 on alkuluku; pi(2)=1; edell. alkuluvut: " + str(Alkuluvut)
    else:
        Alkuluvut.append(2)
        n = 3
        while n < luku:
            if onko_alkuluku(n, Alkuluvut):
                Alkuluvut.append(n)
            n = n + 1
        on_alkuluku = onko_alkuluku(luku, Alkuluvut)
        if on_alkuluku:
            tulos = str(luku)+" on alkuluku; pi(" + str(luku) + ")=" + str(len(Alkuluvut) + 1) + "; edell. alkuluvut: " + str(Alkuluvut)
        else:
            tulos = str(luku)+" ei ole alkuluku; pi(" + str(luku) + ")=" + str(len(Alkuluvut)) + "; edell. alkuluvut: " + str(Alkuluvut)
    return tulos
"""        
print("Tervetuloa alkulukulaskuriin.")

luku = int(input("Anna luku: "))
print(alkulukuTulokset(luku))
"""
