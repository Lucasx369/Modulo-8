# Atividade

## Criação de uma ETL em flask com teste de integração que leia da API OpenWeather, manipule os dados em uma tabela nova guardando as informações em 4 colunas: Data de ingestão, Tipo, Valores, Uso.


**Critérios de Avaliação**
- Criação do aplicativo Flask com Python e configuração correta das dependências
- Configuração dos testes de integração usando bibliotecas como pytest ou unittest
- Consulta à API OpenWeather para obter os dados climáticos de mais de 10 cidades do Brasil
- Manipulação dos dados obtidos para criar uma tabela com as colunas especificadas
- Armazenamento das informações da tabela, incluindo Data da Ingestão, Tipo, Valores e Uso
- Descrição da configuração do Flask, implementação da ETL e armazenamento dos dados

## Descrição Geral

Nesta atividade, está sendo desenvolvida uma aplicação ETL (Extract, Transform, Load) usando Flask. A aplicação interage com a API do OpenWeather para coletar dados meteorológicos de várias cidades do Brasil, processa esses dados e os armazena em um banco de dados local. Abaixo, é realizada uma descrição geral dos arquivos. 

**weather_api.py**

Este arquivo contém o código relacionado à interação com a API do OpenWeather. Isso inclui uma função para fazer solicitações à API, processar a resposta e extrair as informações necessárias.

**app.py**

Este é o arquivo principal do aplicativo Flask. Ele inclui a configuração do Flask, definição de rotas e a lógica para iniciar o processo de ETL. Sendo assim, é o ponto de entrada para o aplicativo.

**data_processor.py**

Este arquivo contém o código para processar os dados obtidos da API do OpenWeather. Isso inclui a transformação dos dados para o formato necessário, como ajustar às colunas da tabela (Data de Ingestão, Tipo, Valores, Uso).

**data_storage.py**

Este arquivo lida com o armazenamento dos dados processados. Ele contém a lógica para salvar os dados na base de dados escolhida.

**test_weather_api.py**

Este arquivo contém os testes de integração para o aplicativo. Ele inclui testes para verificar a integração com a API do OpenWeather.

## Execução


