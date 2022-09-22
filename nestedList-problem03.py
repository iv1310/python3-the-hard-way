"""
Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:

planets = [[‘Mercury’, ‘Venus’, ‘Earth’], [‘Mars’, ‘Jupiter’, ‘Saturn’], [‘Uranus’, ‘Neptune’, ‘Pluto’]]

Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]
"""

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
flatten_planets = []

for subs in planets:
    for val in subs:
        if len(val) < 6:
            flatten_planets.append(val)

print(flatten_planets)

flaaten_planets = [val for x in planets for val in x if len(val) < 6]
print(flaaten_planets)
