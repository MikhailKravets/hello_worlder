import pytest
import redis


@pytest.fixture
def redis_url():
    return "redis://localhost:6379"


@pytest.fixture
def redis_con(redis_url):
    return redis.Redis.from_url(redis_url)
