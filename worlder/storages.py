import typing
import json

import redis


class RedisStorage:
    """A class that has simple API to store / retrieve
    Python dictionaries to Redis

    :param redis_url: full valid URL to the redis DB
    """
    def __init__(self, redis_url: str):
        self.conn = redis.Redis.from_url(redis_url)

    def get(self, key: str) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """Get object with key

        :param key: key of object
        :return: found object or None if there is no such object in Redis
        """
        value = self.conn.get(key)
        if value:
            return json.loads(value)
        return None

    def set(self, key: str, value: typing.Dict[str, typing.Any]):
        """Add object to Redis

        :param key: key of new object
        :param value: object
        """
        value_json = json.dumps(value)
        self.conn.set(key, value_json)

    def flush(self):
        """Flush Redis DB"""
        self.conn.flushdb()
