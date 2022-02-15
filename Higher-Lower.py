import random

# Hier word een module ge-inporteerd waarmee je makkelijk random getallen kan genereren.

import sys, os

# Hier word os ge-inporteerd zodat je de command-line kan leegmaken.

os.system('cls')

print("-----------------------")

naam = input("wat is je naam? ")

os.system('cls')

# hier word het scherm leeg gemaakt

print("------------------------------------------------------------------------------------------")
print(" ")
print("Hallo " + naam + ", welkom bij dit nummer raad spel.")
print("Het doel is om het getal te raden tussen de 1 en de 100.")
print("Wanneer je een getal invoert en op enter drukt krijg je hoger of lager in je beeld te zien.")
print("(Gemaakt door Niels van Rheenen, V4D, Het Streek Lyceum.)")
print("------------------------------------------------------------------------------------------")
print(" ")

nogEenKeer = True

aantalPotjes = 0

totaalAantalPogingen = 0

while nogEenKeer == True:

# Dit is een while loop zodat je gebruikers kan laten kiezen of ze nog een ker willen spelen

    rndGetal = random.randint(1, 100)

    # een random getal wordt gegenereerd tussen de 1 en de 100

    # print(rndGetal) hier word het random getal geprint om te testen

    geraden = False

    aantalPogingen = 0

    aantalPotjes = aantalPotjes + 1

    while geraden == False:

    # In deze while loop word er voor gezord dat je nog een keer een poging kan wagen als je het nummer niet goed hebt geraden

        aantalPogingen = aantalPogingen + 1

        totaalAantalPogingen = totaalAantalPogingen + 1

        poging = input("vul hier je poging in: ")

        # hier word de input van de user gevraagd en gekoppelt aan een variablele

        if int(poging) == rndGetal:
            print("je hebt het nummer goed geraden " + str(rndGetal))
            geraden = True
        elif int(poging) > rndGetal:
            print("lager, probeer het nog een keer")
        else:
            print("Hoger, probeer het nog een keer")

        # in deze if,elif,else statement word er geken naar poging en of hij lager of hoger dan het te raden getal is

    wiltNogEenKeer = input("Wil je nog een keer spelen? `y` om nog een keer te spelen | `n` als je wilt stoppen.")

    # hier word gevraagd of je nog een keer wilt spelen

    if wiltNogEenKeer == "y":
        nogEenKeer = True
        print("------------------------------------------------------")
        print("je hebt het getal zojuist in " + str(aantalPogingen) + " keer geraden.")
        print("------------------------------------------------------")
        aantalPogingen = 0
    else:
        nogEenKeer = False

        os.system('cls')

        print("------------------------------------------------------")
        print("Bedankt voor het spelen " + naam)
        print("je hebt zojuist het getal in " + str(aantalPogingen) + " keer geraden.")
        print("------------------------------------------------------")
        print("Statistieken:")
        print("Je hebt " + str(aantalPotjes) + " potjes gespeelt.")
        print("Je hebt in totaal " + str(totaalAantalPogingen) + " pogingen gewaagd.")

        gemiddeldAantalPogingen = totaalAantalPogingen // aantalPotjes
        
        print("Je hebt per potje gemiddeld " + str(gemiddeldAantalPogingen) + " pogingen gewaagd.")
        print("------------------------------------------------------")

    # hier word er gekeken naar de input van de user of ze nog een keer willen spelen en past dan een boolean aan