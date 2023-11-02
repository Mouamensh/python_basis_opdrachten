# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
# Vragen stellen aan de gebruiker
vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Antwoorden opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("Resultaten van de enquête:\n")
    bestand.write(f"Vraag 1: Wat vind je van de huidige regering? Antwoord: {vraag1}\n")
    bestand.write(f"Vraag 2: Wat vind je van de Python-lessen tot nu toe? Antwoord: {vraag2}\n")
    bestand.write(f"Vraag 3: Wat vind jij de mooiste stad van Nederland? Antwoord: {vraag3}\n")

print("Dank je wel voor het invullen van de enquête. De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")
