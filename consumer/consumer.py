import pika
import time

def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")
    time.sleep(body.count(b'.'))  # Simulate work
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='rabbitmq',  # Change this if using a different service name or host
        credentials=pika.PlainCredentials('rabbitmq', 'rabbitmq')
    )
)
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    main()