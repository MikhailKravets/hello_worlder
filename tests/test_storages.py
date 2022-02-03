import json

from worlder.storages import RedisStorage


def test_set(redis_url, redis_con):
    key, data = "test", {"test": "test"}
    storage = RedisStorage(redis_url)
    storage.set(key, data)

    d = redis_con.get(key)
    assert json.loads(d) == data


def test_get(redis_url, redis_con):
    key, data = "test", {"test": "test"}

    storage = RedisStorage(redis_url)

    redis_con.set(key, json.dumps(data))

    assert storage.get(key) == data


def test_get_key_not_exist(redis_url, redis_con):
    key, data = "test", {"test": "test"}

    storage = RedisStorage(redis_url)

    redis_con.set(key, json.dumps(data))

    assert storage.get("wrong-key-fjeiwfhiuweh") is None


def test_flush(redis_url, redis_con):
    storage = RedisStorage(redis_url)
    storage.flush()

    assert len(redis_con.keys()) == 0
