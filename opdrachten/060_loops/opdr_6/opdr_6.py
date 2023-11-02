# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Oorspronkelijke lijst met pizza's
pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabetische volgorde
pizza_lijst.sort()

# Voeg een pizza toe
pizza_lijst.append('yo-favorito')

# Verwijder de pizza die je het minst lekker vindt (in dit geval 'olivio')
pizza_lijst.remove('olivio')

# Print de eerste 3 pizza's
print(pizza_lijst[:3])

# Print alleen de middelste pizza
print([pizza_lijst[len(pizza_lijst) // 2]])

# Print de laatste 3 pizza's
print(pizza_lijst[-3:])
