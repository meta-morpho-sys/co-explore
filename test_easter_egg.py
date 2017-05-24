
"""
This is a reduced versione of the program that randomly picks an adjective from one list
and matches it with a surname from a second list.
Here the question is how to make the for loop work without printing the phrase * Steve Wozniak is not boring * 
for each caracter of the "new_name" value.
"""

import random


adjectives = [ "admiring", "boring" ]
surnames = [ "boulton", "wozniak" ]


adjective = random.choice(adjectives)
surname = random.choice(surnames)


new_name = (adjective + '_' + surname)
print(new_name)

for easter_egg in new_name:
    if easter_egg == "boring_wozniak":
        continue
    print("* Steve Wozniak is not boring *")

