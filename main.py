from worlder import Hello
from worlder.storages import RedisStorage

REDIS_URL = "redis://localhost:6379"

if __name__ == '__main__':
    name = "Jon Doe"

    r = RedisStorage(REDIS_URL)
    h = Hello(name)

    greeting = h.world()
    print(greeting)

    r.set("greeting", {'greeting': greeting, "name": name})
    print(r.get("greeting"))

    print("Hello world, again!")
