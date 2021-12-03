def megtalal(karakter: str, szoveg: str) ->int:
    """
    A karakter pozíciójának megkeresése.
    :param karakter: Keresendő karakter.
    :param szoveg: Szöveg, amiben keresünk.
    :return: A karakter első előfordulása a szövegben vagy -1, ha nincs benne.
    """
    pozicio = -1   #ezt csak azért hogy átláthatóbbak legyenek a returnök
    for i in range(len(szoveg)):
        if szoveg[i] == karakter and pozicio == -1:
            pozicio = i
    return pozicio

print(megtalal("p", "asofnpdslkfm"))
