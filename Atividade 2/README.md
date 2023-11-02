# Atividade

### Criação de um docker-compose com todos os parâmetros de um kafka e seus gerenciadores e um exemplo de produção e consumo de mensagem local.

**Critérios de Avaliação**
- Criação do docker-compose com os parâmetros do kafka e seus gerenciadores (ex: zookeeper)
- Utilização dos parâmetros (como Endpoint de conexão de filas) baseados na documentação da Apacha Kafka
- Implementação funcional de um exemplo de produção e consumo de mensagem utilizando o kafka
- Descrição clara dos parâmetros utilizados no docker-compose, em comentários no código ou no readme
- Explicação do exemplo de produção e consumo de mensagem na documentação

## Documentação
### Descrição Geral

**Objetivo Geral**: Criar um ambiente Docker com Kafka e ZooKeeper.
- Passo 1: Usar o Docker Compose para configurar Kafka e ZooKeeper.
- Passo 2: Configurar o Kafka.
- Passo 3: Criar um exemplo funcional que demonstre a produção e consumo de mensagens com Kafka.

Passos Completos:[Manual](https://github.com/Lucasx369/Modulo-8/tree/main/Atividade%202/src)

### Docker
O docker é um software usado para implantar aplicativos dentro de containers virtuais. A conteinerização permite que vários aplicativos funcionem em diferentes ambientes complexos. Assim, o objetivo dos containers é criar independência: a habilidade de executar diversos processos e apps separadamente para utilizar melhor a infraestrutura e manter a segurança.

Referência: [Docker: desenvolvimento de aplicações em containers](https://www.redhat.com/pt-br/topics/containers/what-is-docker)

### Kafka
O Apache Kafka (Figura 1) é uma plataforma de streaming distribuído capaz de manipular trilhões de eventos por dia. A ferramenta foi inicialmente concebida como uma fila de mensagens, porém rapidamente evoluiu para um plataforma de streaming completa (com a capacidade de armazenar e processar os dados em um fluxo.). 

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%202/assets/kafka.png">

**Figura 1**. Arquitetura do Kafka. Fonte: Arquivo pessoal.

**Principais Características**
- Baixa latência: Capacidade de processar e entregar um alto fluxo de dados com pouco/mínimo atraso.
- Tolerância a falhas: Garantia do funcionamento do sistema mesmo em caso de falhas.


**Funcionamento**
Um aspecto fundamental da arquitetura do Kafka é que os produtores de dados enviam mensagens para tópicos, e essas mensagens são particionadas e distribuídas entre os brokers. Os consumidores podem se inscrever nos tópicos e ler dados de qualquer uma das partições. Isso permite que o Kafka dimensione horizontalmente e lide com cargas massivas de leituras e gravações por segundo.


- Cluster: é um conjunto de servidores (ou brokers) Kafka que trabalham juntos para fornecer escalabilidade, alta disponibilidade e tolerância a falhas para a plataforma Kafka. 
- Broker: é um nó individual no cluster Kafka. Cada broker é responsável por armazenar e gerenciar partições de tópicos, bem como lidar com solicitações de produtores e consumidores
- Topic: é uma categoria no qual as mensagens são publicadas pelos produtores e consumidas pelos consumidores. Cada tópico representa um fluxo de mensagens relacionadas a um tópico específico, como logs de servidores, eventos de sensores, registros de pedidos, entre outros. Os tópicos são identificados por nomes, e as mensagens são publicadas em tópicos com base em sua relevância.
- Partitions: são divisões do kafka topic, sendo ordenadas e compostas por um log de mensagens. Essas mensagens são anexadas à partição na ordem em que são recebidas. Além disso, as partições permitem que o Kafka distribua o processamento e o armazenamento de mensagens em vários brokers.
- Producer: são responsáveis por mapear cada mensagem para uma partição do tópico. Isso é geralmente feito com base em uma chave ou algoritmo de particionamento. 
- Consumer: são responsáveis por ler mensagens de partições específicas de um tópico. Cada Consumer lê de uma ou mais partições, dependendo de como são configurados.

Referência: [Apache Kafka](https://medium.com/trainingcenter/apache-kafka-838882261e83)
### Zookeeper
O Apache ZooKeeper é um serviço centralizado para manter informações de configuração, nomear, fornecer sincronização distribuída e fornecer serviços de grupo. Nesse contexto, ele será usado paracoordenar as ações dos brokers Kafka em um cluster.

Referência: [Apache ZooKeeper](https://docs.aws.amazon.com/pt_br/emr/latest/ReleaseGuide/emr-zookeeper.html)
