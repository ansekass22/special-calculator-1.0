"Moduuli kokonaisluvun tekijöiden laskemiseksi"
def tekijaLaskuri(n):
    tekijat = [1]
    if n == 0:
        return "----------"
    if n == 1:
        return [1]
    for tek in range(2,int(n/2) + 1):
        if (n % tek) == 0:
            tekijat.append(tek)
    tekijat.append(n)
    return tekijat

#print(tekijaLaskuri(100))
