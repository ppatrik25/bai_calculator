import datetime
import time


def pontos_ido():
    print(datetime.datetime.now())

pontos_ido()


def varakozas(masodperc : int):
    pontos_ido()
    time.sleep(masodperc)
    pontos_ido()

pontos_ido()
varakozas(10)