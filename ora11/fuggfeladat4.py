def get_afa(termek_ara: int, afa = 27) -> float:
    """
    :param termek_ara: A termék ára forintban
    :param afa: Az áfakulcs %-ban
    :return: ...
    """
    return termek_ara * afa / 100

def brutto(termek_ara: int, afa=27) -> float:
    return termek_ara + get_afa(termek_ara, afa)

ar = 10000
print(get_afa(ar))
print(brutto(ar))