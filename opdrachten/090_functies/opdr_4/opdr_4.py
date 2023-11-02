# Opdracht 1 functies
# Naam student:
# Groep:

def volledige_naam(lijst_met_namen):
    for naam_dict in lijst_met_namen:
        voornaam = naam_dict["voornaam"]
        tussenvoegsel = naam_dict["tussenvoegsel"]
        achternaam = naam_dict["achternaam"]

        # Voeg de onderdelen samen met juiste spaties
        volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}".strip()

        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
