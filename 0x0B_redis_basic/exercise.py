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


def replay(fn: Callable):
    """ Display the history of calls of a particular function """
    redis_instance = redis.Redis()
    function_name = fn.__qualname__
    call_count = redis_instance.get(function_name)
    try:
        call_count = call_count.decode('utf-8')
    except Exception:
        call_count = 0
    time_str = "time:" if call_count == 1 else "times:"
    print(f'{function_name} was called {call_count} {time_str}')
    inputs = redis_instance.lrange(function_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(function_name + ":outputs", 0, -1)
    for input_value, output_value in zip(inputs, outputs):
        try:
            input_value = input_value.decode('utf-8')
        except Exception:
            input_value = ""
        try:
            output_value = output_value.decode('utf-8')
        except Exception:
            output_value = ""
        print(f'{function_name}(*{input_value}) -> {output_value}')


class Cache():
    """ Cache class for storing and retrieving data in Redis. """

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

    def get_int(self, key: str) -> int:
        """ Retrieve data as an integer """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value

    def get_str(self, key):
        """ Retrieve data as string """
        value = self._redis.get(key)
        return value.decode("utf-8")
