
import redis
import time

# Connect to the Redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Trigger a background save using the BGSAVE command
r.bgsave()

# Wait a few seconds to allow Redis to perform the save
print("BGSAVE command issued. Waiting for the background save to complete...")

# Optionally, check the status of the save by looking at the Redis info
# This will show you details about the background saving process
info = r.info('persistence')
if info.get('rdb_bgsave_in_progress') == 1:
    print("A background save is currently in progress.")
else:
    print("No background save in progress.")
