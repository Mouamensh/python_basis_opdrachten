# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

aantal_pogingen = 0

print("Raad mijn geheime getal")

while True:
    poging = int(input())
    aantal_pogingen += 1

    if poging < geheim_getal:
        print("hoger")
    elif poging > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break
