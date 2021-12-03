def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()

    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            if rendezett_lista[j] > rendezett_lista[j + 1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j+1]
                rendezett_lista[j+1] = seged

    return rendezett_lista


lista = [42, 12, 76, 23, 51, 23, 36]
print(lista)
print(rendezes(lista))


"""
Egész számokat tartalmazó listában minimum, maximum, átlag, összeg keresés.
"""
def minimum(lista: list[int], hanyadik = 0) -> int:
    return rendezes(lista)[hanyadik]

print(minimum(lista))

def osszeg(lista: list[int]) -> int:
    osszeg = 0
    for elem in lista:
        osszeg += elem
        return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)

print(osszeg(lista))
print(atlag(lista))