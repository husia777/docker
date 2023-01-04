import redis

with redis.Redis(host='redis', port=6379) as client:
    while True:
        problem = input()
        client.lpush('problems', problem)


