def nevkeres() -> str:
    return input("hogy hívnak?\n")

def koszon(nev="") -> None:
    print(f"Szia {nev}!")

koszon()
koszon(nevkeres())