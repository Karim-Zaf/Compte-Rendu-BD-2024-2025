from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Remplacer par votre URL MongoDB

# Base de données : "Université"
db = client['Universite']




# 1. Collection "classe" 
classe = db['classe']

# Insertion de 2 étudiants

classe.insert_many([{
    "nom": "Zaafrani",
    "prenom": "Karim",
    "age": 20,
    "groupe": "Augias",
},{
    "nom": "Amine",
    "prenom": "Marzouk",
    "age": 22,
    "groupe": "Geryon",
}])
print("etudiant inséré avec succès")

#afficher toute la classe 
for etudiant in classe.find({}) : 
    print  (etudiant)

#afficher karim 
print ( classe.find_one({"nom":"Zaafrani"}))