class Kutya:
    """A kutyák osztálya"""

    def __init__(self, nev: str, fajta: str):
        self.nev = nev
        self.fajta = fajta


    def __str__(self):     # mindig stringgel ter vissza
        return "A {} nevű kutya {} fajtájú.".format(self.nev, self.fajta)

kutya1 = Kutya("Bodri", "kuvasz")
kutya2 = Kutya("Buksi", "puli")
print(kutya1)
print(kutya2)
