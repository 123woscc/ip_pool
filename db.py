from config import HOST, PORT, DB_NAME
import redis

redis_pool = redis.ConnectionPool(host=HOST, port=PORT, max_connections=20, decode_responses=True)


class RedisPool():
    def __init__(self):
        self._conn = redis.Redis(connection_pool=redis_pool)

    def gets(self, total=1):
        tmp = self._conn.srandmember(DB_NAME, total)
        return [ip for ip in tmp]

    def puts(self, ips):
        self._conn.sadd(DB_NAME, *ips)

    def pop(self):
        return self._conn.spop(DB_NAME)

    @property
    def size(self):
        return self._conn.scard(DB_NAME)

    def _flush(self):
        self._conn.flushall()
