# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):

    volume = m ** 3
    return volume

    pass

import math

def bol_vol(straal):
    volume = (4/3) * math.pi * straal ** 3
    return volume

    pass
kubus_volume = kubus_vol(5)
bol_volume = bol_vol(4)

print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")
