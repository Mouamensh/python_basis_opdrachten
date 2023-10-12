# Opdracht 1 lists
# Naam student:
# Groep:

# Een lijst aanmaken om de dictionaries op te slaan
personen = []

# Dictionaries aanmaken voor vier personen en toevoegen aan de lijst
persoon1 = {"id": 1, "voornaam": "John", "achternaam": "Doe"}
persoon2 = {"id": 2, "voornaam": "Jane", "achternaam": "Smith"}
persoon3 = {"id": 3, "voornaam": "Alice", "achternaam": "Johnson"}
persoon4 = {"id": 4, "voornaam": "Bob", "achternaam": "Brown"}

personen.extend([persoon1, persoon2, persoon3, persoon4])

# De volledige naam van de tweede persoon afdrukken
print(personen[1]["voornaam"], personen[1]["achternaam"])

