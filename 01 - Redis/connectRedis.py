import redis

r = redis.Redis(
  host='redis-10937.c82.us-east-1-2.ec2.redns.redis-cloud.com',
  port=10937,
  password='YkwYGJidRXUR3urKokCGsjNDlezkTyWK')

print ( "Vous êtes connecté à Redis !" )

r.set("MyName" , "Karim")

name = r.get ("name")

print ("votre Nom est : " , name)

#output : votre Nom est :  b'karim'

#---------------------------------------------------

r.set ("index" , 0)
print ("Votre index avant incrémentation ", r.get("index"))
r.incr("index")
print ("votre index après incrémentation : ", r.get("index"))

# Votre index avant incrémentation  b'0'
# votre index après incrémentation :  b'1'


#---------------------------------------------------

r.hset('user-session:1234', mapping={
    'name': 'Karim Zaafrani',
    "University": 'IUT Villetaneuse',
    "age": 20
})

myMap = r.hgetall('user-session:1234')
print ("Votre map est : ", myMap)

'''
Output : 
Votre map est :  
    {b'name': b'Karim Zaafrani', b'surname': b'Smith',
    b'company': b'Redis', b'age': b'20', 
    b'University': b'IUT Villetaneuse'}
'''

#pour changer le theme tu fait ctrl + k  puis ctrl + t 