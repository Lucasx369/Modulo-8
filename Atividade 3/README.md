# Criação de um lambda com API gateway na AWS em python.
## Descrição Geral
Esta atividade consiste na criação e configuração de uma infraestrutura na AWS para criar um endpoint REST (Representational State Transfer) que utiliza o método POST e requer autenticação. O objetivo é permitir que os usuários acessem uma função Lambda por meio de uma API Gateway.

## Ferramentas Utilizadas 

**AWS Academy**: através desse recurso é possível acessar a AWS Educate, na qual oferece créditos de nuvem, laboratórios práticos e recursos adicionais. Neste ambiente, serão utilizadas AWS Lambda e API Gateway, para criar funções de computação que respondem a eventos, como requisições da API Gateway.

**Visual Studio Code**: é um ambiente de desenvolvimento integrado (IDE) gratuito e de código aberto desenvolvido pela Microsoft. Ele é projetado para ser uma ferramenta versátil e leve que pode ser usada para desenvolver uma ampla variedade de aplicativos, desde aplicativos da web até aplicativos de desktop e serviços em nuvem. 

**Thunder Client**: é uma extensão do Visual Studio Code que é usado para testar APIs diretamente do ambiente de desenvolvimento. 

## Orientação de acesso
No basic authentication inserir:
- Username: lucas
- Senha: inteliabc

## Criar Lambda
**1) Pesquisar Lambda**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/1.png">

**2) Clicar em Criar função**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/2.png">

**3) Preencher os campos:**
- Nome da função;
- Linguagem python, porque é uma linguagem mais performátia, tendo em vista que lambda foi pensada para ela; 
- Arquitetura x86_64, tendo em vista que a performance é maior;
- Selecionar o tópico "Usar uma função existente", posteriormente clicar em LabRole;

Por fim, clicar no botão em Criar função.

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/4.png">

**4) Visão geral da função**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/5.png">

## Criar API Gateway
**1) Adicionar Gatilho e pesquisar API Gateway**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/6.png">

**2) Preencher os campos:**
- Selecionar a opção "Create a new API";
- Selecionar a opção "REST API";
- Em segurança, selecionar a opção "Open";
  
<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/7.png">

**3) Visão geral da API Gateway**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/8.png">

## Modificar API Gateway para POST

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/10.png">

**1) Selecionar a opção POST**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/12.png">

**2) Conceder permissão à função lambda**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/16.png">

**3) Visualização dos gatilhos criados**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/19.png">

## Instalar Thunder Client 
<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/22.png">

**1) Trocar método GET por POST**
<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/23.png">

### Teste sem autenticação

**1) Função lambda sem autenticação**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/25.png">

**2) Imprimir JSON**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/26.png">

### Teste com autenticação
<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/27.png">

## Thunder Cliente

**1) Função lambda com autenticação**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/28.png">

**2) Realizar a autenticação**
No basica authentication inserir:
- Username, por exemplo: lucas;
- Password, por exemplo: inteliabc;
Após a confirmação do acesso, é impresso o JSON.
<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/29.png">

## Criar evento de teste na AWS 

### 1° Teste: Informações de autenticação inválida 

**1) Criar evento de teste**
**Preencher os campos:**
- Nome do evento;
- Configuração de compartilhamento: Privado; 
- Inserir evento de entrada que pode ser usado ao testar a função AWS Lambda;

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/33.png">

**2) Clicar em Test, para testar a função**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/32.png">

**3) Resultado do teste**

**Resultado esperado:** Acesso não autorizado 

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/34.png">

### 2° Teste: Campo vazio

**1) Criar evento de teste**
**Preencher os campos:**

- Nome do evento;
- Configuração de compartilhamento: Privado; 
- Inserir evento de entrada que pode ser usado ao testar a função AWS Lambda;

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/35.png">

**2) Clicar em Test, para testar a função**

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/32.png">

**3) Resultado do teste**

**Resultado esperado:** Acesso não autorizado 

<img width="1000" alt="image" src="https://github.com/Lucasx369/Modulo-8/blob/main/Atividade%203/assets/36.png">

