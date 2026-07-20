from services.redis_service import redis_client

redis_client.set("name", "Dharshan")

print(redis_client.get("name"))