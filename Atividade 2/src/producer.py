from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',  
                        value_serializer=lambda v: str(v).encode('utf-8'))

try:
    while True:
        value = input("Digite uma mensagem para enviar ao Kafka: ")
        producer.send('kafka-python-topic', value=value)
except KeyboardInterrupt:
    producer.close()