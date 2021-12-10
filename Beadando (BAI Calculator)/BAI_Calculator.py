import sys
from datetime import datetime
from enum import Enum


#
# Testzsírszázalék kalkulátor
#


class Testalkat(Enum):
    SOVANY = 1
    EGESZSEGES = 2
    TULSULYOS = 3
    ELHIZOTT = 4


def nev_kereses():
    """
    Függvény a 2. funkcióhoz, mellyel megkeressük a beolvasott nevet a 'lista.txt'-ben és kiírjuk a megfelelő adatokat
    """
    keresett_nev = str(input())
    fajlbol_keres = open("lista.txt")
    sorok = fajlbol_keres.readlines()
    with open("lista.txt") as fajlbol_keres:
        for sorszam, sor in enumerate(fajlbol_keres, 1):
            if keresett_nev in sor:
                nev_sora = sorszam - 1
                nev_sora_copy = nev_sora
                while nev_sora_copy <= nev_sora + 6:
                    print("", sorok[nev_sora_copy].rstrip("\n"))
                    nev_sora_copy += 1
                break
            else:
                menu_opciok()


# Személy ősosztály

class Szemely(object):
    def __init__(self):
        # noinspection PyBroadException
        nev_oke_check = 0
        while nev_oke_check == 0:
            self.nev = str(input("Név: "))
            if all(betu.isalpha() or betu.isspace() for betu in self.nev):
                nev_oke_check = 1
            else:
                print("A név csak betűket tartalmazhat.")
                nev_oke_check = 0
        try:
            self.eletkor = int(input("Életkor: "))
        except:
            print("Az életkor csak egész szám lehet.")
            exit()
        try:
            self.magassag = float(input("Magasság (cm): "))
        except:
            print("A magasság csak szám lehet.")
            exit()
        try:
            self.csipo = float(input("Csípőkerület (cm): "))
        except:
            print("A csípőkerület csak szám lehet.")
            exit()

        self.testzsir = (self.csipo / ((self.magassag / 100) ** 1.5)) - 18

    def __str__(self):
        pass


# Nők osztálya

class Nok(Szemely):
    pass

    def testalkat_nok(self):

        if self.eletkor < 20 or self.eletkor > 79:
            print("A testzsírszázalék 20 éves kortól 79 éves korig számolható.")

        elif 20 <= self.eletkor <= 39:
            if self.testzsir < 21:
                return str(Testalkat(1))
            elif 21 <= self.testzsir <= 33:
                return str(Testalkat(2))
            elif 33 < self.testzsir <= 38:
                return str(Testalkat(3))
            elif self.testzsir > 38:
                return str(Testalkat(4))
        elif 40 <= self.eletkor <= 59:
            if self.testzsir < 23:
                return str(Testalkat(1))
            elif 23 <= self.testzsir <= 35:
                return str(Testalkat(2))
            elif 35 < self.testzsir <= 40:
                return str(Testalkat(3))
            elif self.testzsir > 40:
                return str(Testalkat(4))
        elif 60 <= self.eletkor <= 79:
            if self.testzsir < 25:
                return str(Testalkat(1))
            elif 25 <= self.testzsir <= 38:
                return str(Testalkat(2))
            elif 38 < self.testzsir <= 43:
                return str(Testalkat(3))
            elif self.testzsir > 43:
                return str(Testalkat(4))
        else:
            print("Hibás érték.")

    def __str__(self):

        return testzsir, testalkat


# Férfiak osztálya

class Ferfiak(Szemely):
    pass

    def testalkat_ferfiak(self):
        """
        Férfiak testalkatát megállapító függvény, életkor és testzsírszázalék alapján
        :return: Megfelelő érték Testalkat Enumból (Sovány, Egészséges, Túlsúlyos, Elhízott)
        """
        if self.eletkor < 20 or self.eletkor > 79:
            print("A testzsírszázalék 20 éves kortól 79 éves korig számolható.")

        elif 20 <= self.eletkor <= 39:
            if self.testzsir < 8:
                return str(Testalkat(1))
            elif 8 <= self.testzsir <= 21:
                return str(Testalkat(2))
            elif 21 < self.testzsir <= 26:
                return str(Testalkat(3))
            elif self.testzsir > 26:
                return str(Testalkat(4))
        elif 40 <= self.eletkor <= 59:
            if self.testzsir < 11:
                return str(Testalkat(1))
            elif 11 <= self.testzsir <= 23:
                return str(Testalkat(2))
            elif 23 < self.testzsir <= 29:
                return str(Testalkat(3))
            elif self.testzsir > 29:
                return str(Testalkat(4))
        elif 60 <= self.eletkor <= 79:
            if self.testzsir < 13:
                return str(Testalkat(1))
            elif 13 <= self.testzsir <= 25:
                return str(Testalkat(2))
            elif 25 < self.testzsir <= 31:
                return str(Testalkat(3))
            elif self.testzsir > 31:
                return str(Testalkat(4))
        else:
            print("Hibás érték.")

    def __str__(self):

        return testzsir, testalkat


def menu_opciok():
    """
    Függvény a kezdőmenüre
    """
    print("Válasszon az alábbi menüpontok közül!\n\t0 - Kilépés"
          "\n\t1 - Új személy regisztrálása"
          "\n\t2 - Adatok megtekintése")


# Program kezdete

menu = ""
while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        print("Adja meg a nemét:\n1 - Nő, 2 - Férfi")
        nem_valasztas = input()
        if nem_valasztas == "1":
            uj_no = Nok()
            sys.stderr = object
            testzsir = "{:.1f}".format(uj_no.testzsir)
            testalkat = Nok.testalkat_nok(uj_no).replace("Testalkat.", "")

            fajlba_iras = open("lista.txt", "a")
            fajlba_iras.write("Név: {}\nÉletkor: {}\nMagasság: {} cm\nCsípökerület: {} cm\nTestzsírszázalék: {}%\n"
                              "Testalkat: {}\nHozzáadva: {}\n\n".format(uj_no.nev, uj_no.eletkor, uj_no.magassag,
                                                                        uj_no.csipo, testzsir, testalkat,
                                                                        datetime.today().strftime('%Y.%m.%d.')))
            fajlba_iras.close()
            print("Sikeres regisztráció! (Adatok mentve a 'lista.txt' nevű fájlba)")

        elif nem_valasztas == "2":
            uj_ferfi = Ferfiak()
            sys.stderr = object
            testzsir = "{:.1f}".format(uj_ferfi.testzsir)
            testalkat = uj_ferfi.testalkat_ferfiak().replace("Testalkat.", "")

            fajlba_iras = open("lista.txt", "a")
            fajlba_iras.write("Név: {}\nÉletkor: {}\nMagasság: {} cm\nCsípökerület: {} cm\nTestzsírszázalék: {}%\n"
                              "Testalkat: {}\nHozzáadva: {}\n\n".format(uj_ferfi.nev, uj_ferfi.eletkor,
                                                                        uj_ferfi.magassag,
                                                                        uj_ferfi.csipo, testzsir, testalkat,
                                                                        datetime.today().strftime('%Y.%m.%d.')))
            fajlba_iras.close()
            print("Sikeres regisztráció! (Adatok mentve a 'lista.txt' nevű fájlba)")

        else:
            print("Hibás bemenet.")

    elif menu == "2":
        # noinspection PyBroadException
        try:
            print("Keresett személy neve:")
            nev_kereses()
        except:
            print("Nincs elérhető adat!\n")

    elif menu == "0":
        exit()
    else:
        print("Hibás bemenet.")
