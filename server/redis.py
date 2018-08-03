import os

import redis


redis_url = os.environ.get('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)
