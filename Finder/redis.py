from django.core.cache import cache
from django_redis.cache import RedisCache


def cache_checker(url):
    if cache.get(url):
        print(cache.ttl(url))
        print("cache read")
        return cache.get(url)
    return False

def cache_add(url, info):
    print("cache added")
    cache.set(url, info, timeout=1000000)
    print(cache.ttl(url))