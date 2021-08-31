'''
Laskuri, joka laskee Pascalin kertoimet tietyn asteen funktiolle
(asteluku = Pascalin kolmion kerros)
'''
def pascalCoeff(aste):
    if (aste == 0):
        return [1]
    else:
        kertoimet = [1,1]
        i = 1
        while (i < aste):
            uudet = []
            j = 1
            while(j < len(kertoimet)):
                uudet.append(kertoimet[j-1]+kertoimet[j])
                #print("uudet: ", uudet)
                j += 1
            uudet.insert(0,1)
            uudet.append(1)
            kertoimet = uudet
            #print("uudet: ", uudet)
            i += 1
        return kertoimet
'''
print("Lasketaan Pascalin kertoimet.")
luku = int(input("Anna asteluku: "))
print("Pascalin kertoimet ovat: ", *pascalCoeff(luku))
'''
