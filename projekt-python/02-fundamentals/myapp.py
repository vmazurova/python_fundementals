import physics

hmotnost_tlesa = 75
cas = 2
vaha_na_zemi = physics.vaha_na_zemi(hmotnost_tlesa)
vaha_na_mesici = physics.vaha_na_mesici(hmotnost_tlesa)
energie_ei = physics.energie_ei(hmotnost_tlesa)
vzdalenost_zvuku = physics.vzdalenost_zvuku(cas)
print("Váha je nastavená na 75 kg a čas na 2")
print("Váha na Zemi: {} N".format(vaha_na_zemi))
print("Váha na Měsíci: {} N".format(vaha_na_mesici))
print("Výpočet energie podle Einsteinovy rovnice: {}".format(energie_ei))
print("Vypočet vzdálenosti, kterou zvuk urazí za určitý čas: {}".format(vzdalenost_zvuku))