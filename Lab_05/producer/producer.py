import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

while True:
    current_time = time.time()
    message = f"Current time is {int(current_time)}"
    producer.send('common', message.encode('utf-8'))
    print(f"Sent message: {message}")
    time.sleep(5)
