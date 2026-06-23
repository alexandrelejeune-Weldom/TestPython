import os
import time

adresse1 = r"C:\Users\42031581\Desktop\Projet Python\Input_csv"
adresse2 = r"G:\Mon Drive\TestPython.gsheet"

os.makedirs(adresse2, exist_ok=True)

while True:
    for nom_fichier in os.listdir(adresse1):
        if nom_fichier.endswith(".csv"):
            chemin = os.path.join(adresse1, nom_fichier)
            with open(chemin, "r", encoding="utf-8") as f:
                print("Fichier :", chemin)
                for numero, ligne in enumerate(f, start=1):
                    print(f"{numero}: {ligne.rstrip()}")

            destination = os.path.join(adresse2, nom_fichier)
            os.replace(chemin, destination)
            print("Déplacé vers :", destination)
    time.sleep(2)
