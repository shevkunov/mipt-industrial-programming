import redis

redis_host_name = "redis"

database = redis.Redis(host=redis_host_name)

print("Readed from database: ", database.get("key"))
