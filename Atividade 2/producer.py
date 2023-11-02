"""
from confluent_kafka import Producer

# Configurações do produtor Kafka
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do servidor Kafka
    'client.id': 'python-producer'
}

# Crie um produtor Kafka
producer = Producer(producer_config)

# Tópico para produzir mensagens
topic = 'meu-topico'

try:
    # Produza uma mensagem no tópico
    producer.produce(topic, key='chave-1', value='Mensagem de exemplo')
    producer.flush()
    print('Mensagem enviada com sucesso!')
except Exception as e:
    print(f'Erro ao enviar mensagem: {str(e)}')
"""

from kafka import KafkaProducer
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',  # Correção na porta
                        value_serializer=lambda v: str(v).encode('utf-8'))

# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
while True:
    producer.send('kafka-python-topic', value=random.randint(1, 999))  # Correção na chave 'value'