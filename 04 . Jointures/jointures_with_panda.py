import pandas as pd

# Charger les données depuis les fichiers CSV
test1 = pd.read_csv("test.csv", encoding='latin1')
test2 = pd.read_csv("test1.csv", encoding='latin1')

print(test1)
# Faire la jointure entre test1 et test2 sur la colonne "Prénom et nom"
merged_data = pd.merge(test1, test2, on="Prénom et nom")

# Enregistrer le résultat dans un fichier JSON
merged_data.to_json("jointure.json", orient="records", lines=True)

print("La jointure a été réalisée et le résultat est enregistré dans 'jointure.json'.")
print(merged_data)