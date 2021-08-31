from tkinter import *
from PIL import ImageTk ,Image
import kokonaisLukuFunktiot as nFunc
import pascalKertoimet as psc
import tulonTekijat as tt
import alkulukufunktio as alf


voiPutsata = False  #globaali totuusarvoinen muuttuja, jonka tarkoituksena on mahdollistaa uuden luvun kirjoittaminen näyttöön vanhan tuloksen tilalle
def numeroLisays(luku, putsaa):
    global voiPutsata
    if putsaa:
        naytto.delete(0,END)
        voiPutsata = False
    jono = naytto.get()
    naytto.delete(0,END)
    naytto.insert(0, jono + luku)

def puhdista():
    naytto.delete(0,END)

def poistaViim():
    jono = naytto.get()
    uusiJono = jono[0:-1]
    naytto.delete(0,END)
    naytto.insert(0,uusiJono)

def funktioValitsin(func):
    global lahtoArvo
    global voiPutsata
    if naytto.get() == "":
        lahtoArvo = 0
    else:
        lahtoArvo = int(naytto.get())
    global tulos
    if func == 0:
        tulos = str(nFunc.fibonacci(lahtoArvo))
    elif func == 1:
        tulos = str(nFunc.kolmioLuku(lahtoArvo))
    elif func == 2:
        tulos = str(nFunc.tetraedriLuku(lahtoArvo))
    elif func == 3:
        tulos = str(nFunc.kertoma(lahtoArvo))
    elif func == 4:
        tulos = psc.pascalCoeff(lahtoArvo)
    elif func == 5:
        tulos = tt.tekijaLaskuri(lahtoArvo)
    elif func == 6:
        tulos = alf.alkulukuTulokset(lahtoArvo)
    naytto.delete(0,END)
    naytto.insert(0, tulos)
    voiPutsata = True

juuri = Tk()
juuri.title("Spesiaalilaskin")

juuri.geometry('400x500+300+100')

naytto = Entry(juuri, justify='right', width='35', bd='5', font="Calibri 15")
naytto.grid(row=0, column=0, columnspan=4, padx=3, pady=3) 

tek = Button(juuri,text="Fact", height='5', width='11', command=lambda: funktioValitsin(5))
tek.grid(row=1, column=0)

fib = Button(juuri, text="Fib", height='5', width='11', command=lambda: funktioValitsin(0))
fib.grid(row=1, column=1)

phkol = ImageTk.PhotoImage(file="kolmiluku.png")
kol = Button(juuri, image=phkol, command=lambda: funktioValitsin(1))
kol.grid(row=1, column=2)

phtet = ImageTk.PhotoImage(file="kolmiluku_3D.png")
tet = Button(juuri, image=phtet, command=lambda: funktioValitsin(2))
tet.grid(row=1, column=3)

b7 = Button(juuri, text="7", height='5', width='11', command=lambda: numeroLisays("7", voiPutsata))
b7.grid(row=2, column=0)

b8 = Button(juuri, text="8", height='5', width='11', command=lambda: numeroLisays("8", voiPutsata))
b8.grid(row=2, column=1)

b9 = Button(juuri, text="9", height='5', width='11', command=lambda: numeroLisays("9", voiPutsata))
b9.grid(row=2, column=2)

alk = Button(juuri, text="Prime", height='5', width='11', command=lambda: funktioValitsin(6))
alk.grid(row=2, column=3)

b4 = Button(juuri, text="4", height='5', width='11', command=lambda: numeroLisays("4", voiPutsata))
b4.grid(row=3, column=0)

b5 = Button(juuri, text="5", height='5', width='11', command=lambda: numeroLisays("5", voiPutsata))
b5.grid(row=3, column=1)

b6 = Button(juuri, text="6", height='5', width='11', command=lambda: numeroLisays("6", voiPutsata))
b6.grid(row=3, column=2)

kert = Button(juuri, text="!", height='5', width='11', command=lambda: funktioValitsin(3))
kert.grid(row=3, column=3)

b1 = Button(juuri, text="1", height='5', width='11', command=lambda: numeroLisays("1", voiPutsata))
b1.grid(row=4, column=0)

b2 = Button(juuri, text="2", height='5', width='11', command=lambda: numeroLisays("2", voiPutsata))
b2.grid(row=4, column=1)

b3 = Button(juuri, text="3", height='5', width='11', command=lambda: numeroLisays("3", voiPutsata))
b3.grid(row=4, column=2)

pas = Button(juuri, text="Pasc", height='5', width='11', command=lambda: funktioValitsin(4))
pas.grid(row=4, column=3)

cl = Button(juuri, text="Clear", height='5', width='11', command=puhdista)
cl.grid(row=5, column=0)

back = Button(juuri, text="<-", height='5', width='11', command=poistaViim)
back.grid(row=5, column=1)

b0 = Button(juuri, text="0", height='5', width='11', command=lambda: numeroLisays("0", voiPutsata))
b0.grid(row=5, column=2)

juuri.mainloop()
