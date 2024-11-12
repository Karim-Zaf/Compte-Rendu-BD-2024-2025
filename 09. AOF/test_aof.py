import redis

# Connect to Redis (assuming Redis is running locally)
client = redis.StrictRedis(host='localhost', port=6379, db=0)

try:
    # Check if AOF is enabled
    config = client.config_get('appendonly')

    # Check if the appendonly option was retrieved successfully
    if config is None or b'appendonly' not in config:
        print("Could not retrieve the 'appendonly' configuration. Please check your Redis configuration or permissions.")
    elif config[b'appendonly'].decode() == 'yes':
        print("AOF is already enabled.")
    else:
        print("Enabling AOF...")

        # Enable AOF
        client.config_set('appendonly', 'yes')
        print("AOF has been enabled.")

    # Optionally, trigger a background rewrite of the AOF file
    print("Triggering background rewrite of AOF...")
    client.bgrewriteaof()
    print("Background rewrite triggered. The AOF file will be optimized.")

    # Checking if the AOF file is being rewritten (optional)
    info = client.info('persistence')
    if 'aof_last_bgrewrite_status' in info:
        print("AOF background rewrite status:", info['aof_last_bgrewrite_status'])
except redis.RedisError as e:
    print(f"Redis error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
