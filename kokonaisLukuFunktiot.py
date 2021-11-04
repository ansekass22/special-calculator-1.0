#############################################################
# Oma tekemäni Python-moduuli kokonaislukufunktioista ja -lukujonoista.
# Tehty etupäässä omaa Spesiaalilaskuriohjelmaani varten.
#############################################################
# (C) Antti Kasslin
# 2020
#############################################################

# Palauttaa n.:nnen kolmioluvun k(n), jonka se laskee seuraavasti: k(n)=1+2+3+...+(n-1)+n
# (tiedän, että kolmioluku voidaan laskea yksinkertaisemmin lausekkeella k(n)=n(n+1)/2, mutta 
# tässä moduulissa se lasketaan nyt iteratiivisesti).
def kolmioLuku(n):
    summa = 0
    i = 0
    while i <= n:
        summa += i
        i += 1
    return summa

# Palauttaa n.:nnen tetraedriluvun t(n), joka on n.:nnen ja sitä edeltävien kolmiolukujen summma: t(n)=k(1)+k(2)+k(3)+...+k(n-1)+k(n)
# (tiedän, että tetraedriluku voidaan laskea yksinkertaisemmin lausekkeella t(n)=n(n+1)(n+2)/6, mutta 
# tässä moduulissa se lasketaan nyt iteratiivisesti).
def tetraedriLuku(n):
    summa = 0
    i = 0
    while i <= n:
        summa += kolmioLuku(i)
        i += 1
    return summa

# Laskee Fibonaccin lukujonon n.:nnen jäsenen F(n), joka on F(n)=F(n-1)+F(n-2).
def fibonacci(n):
    summa = 0
    eka = 0    #eka ja toka toimivat alustuksessa Fibonaccin lukujonon 2 ensimmäisenä
    toka = 1   #jäsenenä ja myöhemmin kahtena edellisenä jäsenenä
    i = 2
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while i <= n:
            summa = eka + toka
            eka = toka
            toka = summa
            i +=1
        return summa

# Laskee ja palauttaa kokonaisluvun kertoman n! = 1*2*...*n
def kertoma(n):
    kert = 1
    i=1
    while i <= n:
        kert *= i
        i += 1
    return kert

#for m in range(10):
#print("k(",m,"): ",kolmioLuku(m))
#print("t(",m,"): ",tetraedriLuku(m))
#print("Fib(",m,"): ",fibonacci(m))
#print(m,"!: ",kertoma(m))
#print("+===============+")
