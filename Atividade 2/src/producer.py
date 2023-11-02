from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',  # Correção na porta
                        value_serializer=lambda v: str(v).encode('utf-8'))

# Call the producer.send method with a producer-record
try:
    while True:
        value = input("Digite um valor para enviar ao Kafka: ")
        producer.send('kafka-python-topic', value=value)
except KeyboardInterrupt:
    producer.close()