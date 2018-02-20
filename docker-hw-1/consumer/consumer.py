import pika, redis

redis_host_name = "redis"
pika_host_name = "rabbit"
queue_name = "hello_queue"

database = redis.Redis(host=redis_host_name)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=pika_host_name)
)
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def callback(channel, method, properties, body):
    print("Callback got: ", body)
    try:
        database.set("key", body)
    except redis.RedisError as e:
        print("RedisErros: ", e)


channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()

