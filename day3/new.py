cities = ["Addis Ababa", "Adama",
"Hawassa", "Bahir Dar"]
cities.append("Harar")
cities.insert(2,"gonder")
len(cities) # 6
print(cities) # ['Addis Ababa', 'Adama', 'gonder', 'Hawassa', 'Bahir Dar', 'Harar']
cities.pop(1)
cities.reverse()
cities.remove("Addis Ababa")
len(cities) # 5
print(cities)
cities.sort()
len(cities) # 5
print(cities) # ['Addis Ababa', 'gonder', 'Hawassa', 'Bahir Dar', 'Harar']
