import json
from pymongo import MongoClient
import time

# Connexion à MongoDB
mongo_client = MongoClient("localhost", 27017)

# Choix de la base de données
database = mongo_client['DatabasePerformanceTest']

# Collection sans index
no_index_collection = database['collection_test_no_index']

# Charger les données du fichier JSON
with open('DEM-1_1.json', 'r') as file:
    data_entries = json.load(file)

# Mesurer le temps d'insertion sans index
start_no_index = time.time()
insertion_result_no_index = no_index_collection.insert_many(data_entries)
end_no_index = time.time()
time_no_index = end_no_index - start_no_index

# Collection avec index
indexed_collection = database['collection_test_with_index']

# Création d'un index sur un champ particulier (ex: champ "salutation")
indexed_collection.create_index("salutation")

# Mesurer le temps d'insertion avec index
start_with_index = time.time()
insertion_result_with_index = indexed_collection.insert_many(data_entries)
end_with_index = time.time()
time_with_index = end_with_index - start_with_index

# Affichage des résultats
print(f"Durée sans index : {time_no_index} secondes")
print(f"Durée avec index : {time_with_index} secondes")

# Fermer la connexion MongoDB
mongo_client.close()
