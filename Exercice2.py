import csv

with open("C:\\Users\\Ryanl\\2C3-Travail_Pratique2_H24\\pokemon.csv","r") as fichier:
    pokemons = {}
    data = csv.reader(fichier)
    for ligne in data:
        stats = list(ligne[1:])
        stats_int = [int(element) for element in stats]
        pokemons.update({str(ligne[0]) : stats_int})
    for noms, stats in pokemons.items():
        print(f"{noms} : {stats}")
    print(isinstance(pokemons, dict), isinstance(pokemons["Pikachu"], list), isinstance(pokemons["Pikachu"][0], int))