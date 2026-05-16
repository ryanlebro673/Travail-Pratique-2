import json
import csv

descriptions = [["reel","imaginaire"]]

with open("C:\\Users\\Ryanl\\2C3-Travail_Pratique2_H24\\data.json","r") as fichier:
    data = json.load(fichier)
    with open("C:\\Users\\Ryanl\\2C3-Travail_Pratique2_H24\\data.csv","w") as file:
        ecriture = csv.writer(file)
        for ligne in descriptions:
            ecriture.writerow(ligne)
        
        for ligne in data:
            ligne_str = [str(element) for element in ligne]
            print(ligne_str)
            file.write(','.join(ligne_str) + '\n')
    with open("C:\\Users\\Ryanl\\2C3-Travail_Pratique2_H24\\data.csv", "r") as fichero:
        print(fichero.read())