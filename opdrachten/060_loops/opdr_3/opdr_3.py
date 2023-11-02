# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Maak een lege lijst om de resultaten op te slaan
resultatenlijst = []

# Gebruik een for-loop en de range-functie om de berekeningen uit te voeren
for nummer in range(3, 82, 3):
    kwadraat = nummer ** 2
    gedeeld_door_3 = kwadraat / 3.0
    resultatenlijst.append(gedeeld_door_3)

# Print de lijst op het scherm
print(resultatenlijst)
