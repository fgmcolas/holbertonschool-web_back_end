#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator that counts the number of times a function is called """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and outputs for a function """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        input_key = key + ":inputs"
        output_key = key + ":outputs"
        data = str(args)
        self._redis.rpush(input_key, data)
        output = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


def replay(func: Callable):
    """ Display the history of calls of a particular function """
    redis_instance = redis.Redis()
    key = func.__qualname__
    input_key = "{}:inputs".format(key)
    output_key = "{}:outputs".format(key)
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)
    calls_number = len(inputs)
    times_str = 'times' if calls_number != 1 else 'time'
    print(f"{key} was called {calls_number} {times_str}: ")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{key}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


class Cache():
    def __init__(self):
        """ Initialize the Cache with a Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis with a random key
        and return the key as string """
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Get data as a string """
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
