import pandas as pd

def csv_to_json_with_panda(csv_file):
    # étape 1: Lire le fichier CSV en utilisant pandas
    df = pd.read_csv(csv_file, encoding='latin1')

    # étape 2: Convertir le CSV en JSON
    json_data = df.to_json(orient='records', force_ascii=False)

    # étape 3: Enregistrer le JSON résultant
    print (json_data)
    
    return json_data

data = csv_to_json_with_panda("test.csv")
file = open("test.json", "w")
file.write(data)
