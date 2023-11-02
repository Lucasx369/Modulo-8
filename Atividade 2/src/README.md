# Documentação

### Docker-Compose
Neste arquivo são criados dois serviços, Zookeeper e Kafka, para criar um ambiente de mensagens em tempo real.

```yml
# Define a versão do Docker Compose
version: '3'

# Define os serviços que serão criados
services:
  #Define o zookeper
  zookeeper:
    # Imagem Docker que será usada para criar o contêiner
    image: confluentinc/cp-zookeeper:latest
    # Váriaveis de ambiente para o conteiner
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
    # Mapeia a porta 2181 do contêiner para a porta 2181 do host
    ports:
      - "2181:2181"

  #Define o kafka
  kafka:
    # Imagem Docker para criar o contêiner Kafka
    image: confluentinc/cp-kafka:latest
    # Define que o serviço Kafka depende do serviço Zookeeper.
    depends_on:
      - zookeeper
    # Váriaveis de ambiente
    environment:
      # Identificação do broker
      KAFKA_BROKER_ID: 1
      # Porta e endereço de conexão
      KAFKA_LISTENERS: PLAINTEXT://:9092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      # Porta de conexão com o zookeeper
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    # Mapeia a porta 9092 do contêiner para a porta 9092 do host
    ports:
      - "9092:9092"
```

**Inicialização:**

```
docker-compose up
```

### Producer
Neste arquivo é criado um produtor Kafka que permite ao usuário digitar mensagens que são enviadas para um tópico Kafka local chamado 'kafka-python-topic'. 

```python
# Importar classe para criar um produtor Kafka
from kafka import KafkaProducer

# Especifica o endereço do servidor Kafka e define função de serialização dos valores 
producer = KafkaProducer(bootstrap_servers='localhost:9092',  
                        value_serializer=lambda v: str(v).encode('utf-8'))
# Loop de produção de mensagens
try:
    while True:
        # Recebe mensagem
        value = input("Digite uma mensagem para enviar ao Kafka: ")
        # Mensagem é enviada para o tópico
        producer.send('kafka-python-topic', value=value)
# Encerrar o programa
except KeyboardInterrupt:
    producer.close()
```

**Inicialização:**

```
python producer.py
```

### Consumer

Neste arquivo é criado um consumidor Kafka que se conecta a um servidor Kafka local na porta 9092, consome mensagens do tópico 'kafka-python-topic' e imprime o conteúdo das mensagens no console.

```javascript
// Importar módulo para criar consumidor Kafka 
const Kafka = require('no-kafka');

// Especifica o endereço e a porta de conexão do servidor Kafka
const consumer = new Kafka.SimpleConsumer({ connectionString: '127.0.0.1:9092' }); 

# Função de tratamento e impressão da mensagem
var data = function (messageSet) {
    messageSet.forEach(function (m) {
        var value = m.message.value.toString('utf8');
        #Imprimir mensagem
        console.log(value);
    });
};

// Inicializar o consumidor
return consumer.init().then(function () {
    //Inscrever consumidor no tópico para consumir conteúdo
    return consumer.subscribe('kafka-python-topic', data);
});
```

**Inicialização:**

```
node consumer.js
```
