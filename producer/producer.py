import pika
import time

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

    while True:
        message = input("Enter message: ")
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
            ))
        print(f"Sent: {message}")

    connection.close()

if __name__ == "__main__":
    main()