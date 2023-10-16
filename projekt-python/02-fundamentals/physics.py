'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def vaha_na_zemi(hmotnost):
    """Funkce vypočítá váhu tělesa na zemi. Je použit parametr hmotnost a konstanta gravitace na Zemi"""
    return hmotnost * EARTH_GRAVITY

def vaha_na_mesici(hmotnost):
    """Funkce vypočítá vahu na Měsíci. Je použit parametr hmotnost a konstanta gravitace na Měsíci"""
    return hmotnost * MOON_GRAVITY

def energie_ei(hmotnost):
    """Funkce vypočítá energii podle Einsteinovy rovnice. Je do ní poslán parametr hmotnost a konstanta rychlost světla"""
    energie = hmotnost * SPEED_OF_LIGHT**2
    return energie
def vzdalenost_zvuku(cas):
    """Funkce vypočítá vzdálenost, kterou zvuk urazí za určitý čas. Využit taktéž parametr a a konstanta rychlost zvuku"""
    vzdalenost = SPEED_OF_SOUND * cas
    return vzdalenost
print(vaha_na_zemi.__doc__)
print(vaha_na_mesici.__doc__)
print(energie_ei.__doc__)
print(vzdalenost_zvuku.__doc__)

