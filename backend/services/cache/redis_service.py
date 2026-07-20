import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

CACHE_TTL = 3600  # 1 Hour

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
)


def get_cached_answer(question: str):
    """
    Retrieve a cached answer from Redis.
    """

    return redis_client.get(question)


def cache_answer(question: str, answer: str) -> None:
    """
    Store an answer in Redis with a TTL.
    """

    redis_client.setex(
        name=question,
        time=CACHE_TTL,
        value=answer,
    )


def delete_cached_answer(question: str) -> None:
    """
    Remove a cached answer from Redis.
    """

    redis_client.delete(question)


def clear_cache() -> None:
    """
    Clear all Redis cache entries.
    Use only for development or testing.
    """

    redis_client.flushdb()