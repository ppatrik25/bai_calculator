def kacsanevek(prefixes='JKLMNOPQ', suffix='ack') -> list[str]:
    nevek = []
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu + suffix)
        return nevek

print(kacsanevek())