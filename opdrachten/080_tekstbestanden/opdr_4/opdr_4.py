# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


vragen = ["Wat is je voornaam?", "Wat is je achternaam?", "Wat neem je mee aan drank?", "Wat neem je mee om te eten?"]

feestgangers = []

while True:
    antwoorden = {vraag: input(vraag) for vraag in vragen}
    feestgangers.append(antwoorden)

    nog_een = input("Wil je nog een feestganger toevoegen? (ja/nee) ")
    if nog_een.lower() != "ja":
        break

with open("feestgangers.txt", "w") as bestand:
    for feestganger in feestgangers:
        bestand.write("----\n")
        for vraag, antwoord in feestganger.items():
            bestand.write(f"{vraag}\n{antwoord}\n")
        bestand.write("----\n")

print("Bedankt voor het invullen!\nSee you at the party.")
