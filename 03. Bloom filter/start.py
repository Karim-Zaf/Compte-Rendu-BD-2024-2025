import redis

# Connexion à Redis
r = redis.Redis()

# Création d'un Bloom filter
try:
    r.bf().create("bloom", 0.01, 1000)
    print("Bloom filter créé avec succès.")
except redis.exceptions.ResponseError as e:
    print(f"Erreur : {e}")
