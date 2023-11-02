"""
from confluent_kafka import Consumer, KafkaError

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest' 
}

consumer = Consumer(consumer_config)

# Inscreva-se em um tópico
topic = 'meu-topico'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0) 

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f'Erro no consumo: {msg.error()}')
                break

        print(f'Recebido mensagem: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
"""
