# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om een lijst met steden in te voeren
input_string = input("Voer minimaal 5 steden in, gescheiden door komma's: ")

# Splits de invoer op basis van komma's en verwijder eventuele extra spaties
steden = [stad.strip() for stad in input_string.split(',')]

# Filter de steden die met "Z" beginnen
z_steden = [stad for stad in steden if stad.startswith("Z")]

# Sorteer de lijst in omgekeerde volgorde
z_steden.sort(reverse=True)

# Verwijder de steden die met "Z" beginnen uit de oorspronkelijke lijst
steden = [stad for stad in steden if not stad.startswith("Z")]

# Voeg de gesorteerde "Z"-steden weer vooraan toe aan de lijst
steden = z_steden + steden

# Druk de gesorteerde lijst af
print(steden)
