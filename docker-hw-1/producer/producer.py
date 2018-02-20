import pika

pika_host_name = "rabbit"
queue_name = "hello_queue"
exit_str = "exit"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=pika_host_name)
)
channel = connection.channel()
channel.queue_declare(queue=queue_name)

print("Producer: enter any string to send or %s to exit" % (exit_str))

while True:
    s = input()
    if (s == exit_str):
        break
    else:
        print("Sending :", s)
        channel.basic_publish(exchange="", routing_key=queue_name, body=s)
