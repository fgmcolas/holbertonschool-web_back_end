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
        self._redis_incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and outputs for a function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable):
    """ Display the history of calls of a particular function """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    redis_instance = method.__self__._redis

    call_count = redis_instance.get(method.__qualname__)
    call_count = int(call_count) if call_count else 0
    print(f"{method.__qualname__} was called {call_count} times: ")

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")



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
