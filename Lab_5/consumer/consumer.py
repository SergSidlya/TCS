from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'common', 
    bootstrap_servers=['kafka:9092'], 
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group')

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
