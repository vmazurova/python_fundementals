def harryPotter():
    harry = input("Zadej jmého známého 7 sériového filmu, ve kterém se objevuje postava jménem 'Severus Snape'")
    if harry.lower() == "harry potter":
        print("Spravne, dalsí otázka:")
    else:
        print("spatne zkus znovu")
        harryPotter()
def obecnaSkola():
    skola = input("Zadej jmého učitele ve filmu Obecná škola:")
    if skola.lower() == "igor hnizdo":
        print("Spravne dalsi otazka")
    elif skola == "Igor Hnizdo":
        print("Spravne dalsi otazka")
    else:
        print("Spatne, zadej znovu")
        obecnaSkola()

def prezident():
    vstupprez= input("Jaké je jméno momentálního prezidenta?\n")
    if vstupprez.lower()=="petr pavel":
        print("SPRAVNĚ")
    else:
        print("Zkus znovu")
        prezident()

def jablko():
    print("Kdo všechno má něco společného s jablkem? Možnosti: Steve Jobs, Zeman, Babiš, Putin, Adam a Eva")
    vstupjablko = input("Zadej v tomto tvaru: jméno, jméno\n")
    if vstupjablko.lower()=="steve jobs, adam a eva":
        print("Spravne, posledni otazka")
    else:
        print("Zkus znovu")
        jablko()

def cisla():
    polePrvku = [5,56,23,85,12,45,26,1,28]
    for prvek in polePrvku:
        print(prvek, end=" ")

    print("\n")
    vstup= input("Které číslo je největší?")
    try:
        celyvstup=int(vstup)
    except:
        print("Nebylo zadano cele cislo, zadej znovu")
        cisla()
    if celyvstup == 85:
        print("Spravne, prošel jsi testem :D")
    else:
        print("špatně, zkus znova\n")
        cisla()
harryPotter()
obecnaSkola()
prezident()
jablko()
cisla()


