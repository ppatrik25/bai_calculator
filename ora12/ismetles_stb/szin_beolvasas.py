def beolvasas(filepath: str):
    szinek = {}
    fileobject = open(filepath, "r")
    for row in fileobject:
        row_datas = row.strip().split("\t")
        szinek[row_datas]



szin_szotar = beolvasas("color.csv")
print(type(szin_szotar))
print(type(szin_szotar["Narancs"]))
print(len(szin_szotar))
print(len(szin_szotar["Narancs"]))
print(szin_szotar.get("kutya", "nincs ilyen szín"))
print("Kutya" in szin_szotar)
print(szin_szotar.keys())
print(szin_szotar.values())
print(szin_szotar.items())
szin_szotar2 = szin_szotar.copy()
szin_szotar3 = szin_szotar
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3)
del(szin_szotar2["Narancs"])
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3)
szin_szotar3.clear()
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3)