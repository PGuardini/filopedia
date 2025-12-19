<div align="center">
    <h1>Filopedia</h1>
    <p>Aplicação web para divulgação de filosofia através de web scraping</p>
</div>

# Introdução

Este projeto é tem como objetivo a divulgação de conteúdo filosófico por meio de camadas de aprofundamento. Temos como objetivo a difusão de história da filosofia, da história das filósofas e dos filósofos e de conceitos filosóficos, possuindo como pilar norteador o livre fluxo do conhecimento ao lado do rigor filosófico.

- [Introdução](#introdução)
  - [Sobre o projeto](#sobre-o-projeto)
  - [Estrutura do projeto](#estrutura-do-projeto)
- [Instalação do projeto](#instalação-do-projeto)
  - [Instalando com Docker](#instalando-com-docker)
- [Utilização](#utilização)
- [Dúvidas? Ideias?](#dúvidas-ideias)
- [Contribuição](#contribuição)


## Sobre o projeto


O projeto tem como base para a criação de cards informativos diários os artigos da Wikipedia, extraídos através de web scraping pela biblioteca [Scrapy][scrapy].

Entendemos a dificuldade para manter o rigor em relação ao conteúdo extraído da Wikipedia, mantendo em mente que é um conteúdo aberto e passível de alteração por qualquer pessoa usuária. Entretanto, como passo inicial para o projeto, como camada superficial, aderimos aos artigos da Wikipedia por sua disponibilidade de copyright, que nos permite a utilização indiscriminada, pedindo somente a referência da página utilizada.

## Estrutura do projeto

# Instalação do projeto

## Instalando com Docker

Você pode usar o arquivo `compose.yaml` para iniciar um container com todas as dependências necessárias

      docker compose -f compose.yaml up -d

O container já estará rodando a aplicação Django na porta local 8000. Para acessá-la, basta acessar no seu navegador `localhost:8000`


Os comandos a seguir devem ser rodados dentro do container
Use `docker exec` para abrir um terminal dentro do container
    
    docker exec -it filopedia-django bash

# Utilização

# Dúvidas? Ideias?

# Contribuição

[scrapy]: https://www.scrapy.org/