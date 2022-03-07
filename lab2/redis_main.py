import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Create a key with a value
r.set('telematica', 'hola mundo')

# Get the value of the key and print value
print(r.get('telematica'))

# Update a key value
r.set('telematica', 'hola telematica')

# Delete a key
r.delete('telematica')

#Create a multiple keys
r.mset({'gog': 'www.google.com', 'eaf': 'www.eafit.edu.co'})

# Get the value of the keys and print values
print(r.mget('gog', 'eaf'))

#Create a value to increment
r.set('count', 50)

# Increment the value of the key
r.incr('count')