import redis

with redis.Redis(host='redis', port=6379) as client:
    while True:
        problem = client.brpop('problems')[1].decode('utf-8')
        print(eval(problem))
