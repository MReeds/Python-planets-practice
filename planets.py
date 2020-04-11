planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

# planet_list.extend(["Jupiter, Saturn"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

# print(planet_list[0:4])

del planet_list[-1]

# print(planet_list)

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

# Iterate over your list of planets, 
# and inside that loop, iterate over 
# the list of tuples. Print, for each planet, 
# which satellites have visited it.

for planet in planet_list:
    for craft in spacecraft:
        if planet in craft:
            print(craft)