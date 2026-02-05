<div align="center">
    <h1>Filopedia</h1>
    <p>Aplicação web para divulgação de filosofia através de web scraping</p>
</div>

# Introdução

Este projeto tem como objetivo a divulgação de conteúdo filosófico por meio de camadas de aprofundamento. Temos como objetivo a difusão de história da filosofia, da história das filósofas e dos filósofos e de conceitos filosóficos, possuindo como pilar norteador o livre fluxo do conhecimento ao lado do rigor filosófico.

- [Introdução](#introdução)
  - [Sobre o projeto](#sobre-o-projeto)
  - [Estrutura do projeto](#estrutura-do-projeto)
- [Instalação do projeto](#instalação-do-projeto)
  - [Instalando o projeto localmente usando PIP](#instalando-o-projeto-localmente-usando-pip)
    - [Executando comandos na venv](#executando-comandos-na-venv)
  - [Instalando o projeto localmente usando UV](#instalando-o-projeto-localmente-usando-uv)
  - [Instalando com Docker](#instalando-com-docker)
    - [Executando comandos no container](#executando-comandos-no-container)
- [Utilização](#utilização)
  - [Rodando o crawler:](#rodando-o-crawler)
    - [Aranha mapeadora](#aranha-mapeadora)
    - [Aranha Wikipedia](#aranha-wikipedia)
  - [Rodando a aplicação Django:](#rodando-a-aplicação-django)
- [Dúvidas? Ideias?](#dúvidas-ideias)
  - [Contatos](#contatos)
- [Contribuição](#contribuição)
  - [Deseja contribuir com o projeto?](#deseja-contribuir-com-o-projeto)
    - [Primeira vez contribuindo?](#primeira-vez-contribuindo)



## Sobre o projeto


O projeto tem como base para a criação de cards informativos diários os artigos da Wikipedia, extraídos através de web scraping pela biblioteca [Scrapy][scrapy].

Entendemos a dificuldade para manter o rigor em relação ao conteúdo extraído da Wikipedia, mantendo em mente que é um conteúdo aberto e passível de alteração por qualquer pessoa usuária. Entretanto, como passo inicial para o projeto, como camada superficial, aderimos aos artigos da Wikipedia por sua disponibilidade de copyright, que nos permite a utilização indiscriminada, pedindo somente a referência da página utilizada.

## Estrutura do projeto

O projeto está dividido em três grandes partes:
- Crawler - sendo `crawler/` o diretório correspondente
- Camada de persistência - sendo `data/` o diretório correspondente
- Projeto Django - sendo `filopedia/` o diretório correspondente

O Crawler é o motor de extração dos dados que serão consumidos pelo projeto Django. Ele utiliza como biblioteca principal o Scrapy, que extrai através das aranhas (spiders) os dados sobre filosofia.

Os dados extraídos pelo Crawler são armazenados na camada de persistência, isto é, no diretório `data/`

Após serem salvos na camada de persistência, a aplicação Django os consome para gerar os cards.

# Instalação do projeto

## Instalando o projeto localmente usando PIP

A instalação recomendada é usando um [ambiente virtual (venv)](venv).

Na raiz do projeto, execute no terminal os seguintes comandos:

```bash
>>> python3 -m venv .venv
    
>>> source .venv/bin/activate (ou: .venv/scripts/activate)

>>> pip3 install -r requirements.txt
```

Após executar `pip3 install`, serão instaladas todas as dependências do projeto, o que permitirá com que ele rode normalmente.

### Executando comandos na venv
> Obs.: toda vez que for executar o projeto localmente, não esqueça de ativar a venv com o comando `source .venv/bin/activate` ou `.venv/scripts/activate`. Após ativar a venv, poderão ser rodados os comandos do projeto no terminal com a venv ativada

---

## Instalando o projeto localmente usando UV

Caso você já possua o UV instalado, pode executar os comandos abaixo para realizar a instalação local do projeto.

```bash
>>> uv sync
```

ou, caso se sinta mais confortável com o requirements.txt:

  Cria o ambiente virtual

```bash
>>> uv venv
```

  Faz a instalação dos pacotes usados no projeto

```bash
>>> uv pip install -r requirements.txt
```
---

## Instalando com Docker

Caso deseje instalar o projeto utilizando o [Docker](docker), você pode usar o arquivo `compose.yaml` para iniciar os containers com todas as dependências necessárias.

No terminal da raiz do projeto, execute o comando:

```bash
>>> docker compose up --build -d
```
O container já estará rodando a aplicação Django na porta local 8000. Para acessá-la, basta acessar no seu navegador <http://localhost:8000>

Para parar os containeres:
```bash
>>> docker compose down
```

### Executando comandos no container
Para executar comandos dentro do container, use `docker exec` para abrir um terminal dentro do container

```bash    
>>>docker exec -it filopedia bash
```

# Utilização

Agora que o projeto está instalado, temos algumas formas de utilizá-lo.

Como foi dito [anteriormente](#estrutura-do-projeto), o projeto é dividido em três grandes partes: crawler, camada de persistência e aplicação Django. A camada de persistência não possui lógica para interagir, portanto ela não possui comandos a serem executados.

O crawler, que tem como função extrair os dados que serão utilizados, possui alguns comandos para ser utilizado.

## Rodando o crawler:

### Aranha mapeadora
Para fazer a extração dos links que serão utilizados pela aranha que extrai os dados, é necessário utilizar o comando abaixo no terminal [local](#executando-comandos-na-venv) (se estiver rodando o projeto localmente) ou no terminal do [container](#executando-comandos-no-container) (se estiver utilizando Docker)

Dentro da pasta `crawler/`, execute o comando:
    
```bash
>>> scrapy crawl mapeadora
```
Esse comando irá abrir a aranha mapeadora que irá popular o arquivo `urls.json` dentro da pasta `crawler/scrapers/`. Esse arquivo possui todos os links atualizados da lista de temas de filosofia listados no site da [Stanford Encyclopedia of Philosophy](SEP-contents), que utilizamos como base.

---

### Aranha Wikipedia

Após ter rodado a aranha mapeadora e populado o arquivo `urls.json` com a lista atualizada de conteúdos de filosofia, você pode começar a fazer a extração dos dados da wikipedia sobre os temas de filosofia listados.

Na pasta `crawler/`, execute no terminal o comando:

```bash
>>> scrapy crawl wikipedia
```
  A aranha wikipedia irá iniciar a extração e começará a criar arquivos .json na pasta `data/`, consolidando os dados extraídos na camada de persistência, que serão consumidos mais tarde pela aplicação Django.

> Obs.: Para saber sobre aranhas do scrapy, veja este [link](spiders-scrapy)

## Rodando a aplicação Django:

Caso você esteja utilizando o projeto através do Docker, a aplicação Django já estará rodando em <http://localhost:8000>.

Se você estiver rodando o projeto localmente, será necessário rodar o servidor Django no terminal da venv.

Na pasta `filopedia/`, execute o seguinte comando no terminal da venv:

```bash
>>> py manage.py runserver (ou apenas manage.py runserver)
```

Caso esteja usando UV (não precisa ativar a venv):

```bash
>>> uv py run manage.py runserver
```

Obs.: se estiver executando na raiz do projeto, o caminho se torna `filopedia/manage.py`

Agora é para o servidor Django estar rodando em <http://localhost:8000> no seu navegador.

# Dúvidas? Ideias?

O projeto Filopedia é um projeto opensource que visa a divulgação de conteúdo de filosofia com o máximo de rigor possível, visando a acessibilidade para pessoas que não são do meio acadêmico.

Possui alguma dúvida ou ideia sobre o projeto?

Estamos abertos para ouvir você e dispomos os contatos abaixo para receber qualquer tipo de dúvida, ideias, críticas etc.

## Contatos

- E-mail: [pguardini.trabalho@gmail.com](mailto:pguardini.trabalho@gmail.com)
- Instagram: [instagram.com/pedro_gabiatti/](https://www.instagram.com/pedro_gabiatti/)
- LinkedIn: [linkedin.com/in/pedroguardini](https://linkedin.com/in/pedroguardini)

# Contribuição

## Deseja contribuir com o projeto?

Visite a [página de issues da filopedia](filopedia-issues) e encontre uma issue com a qual você gostaria
de trabalhar e que ainda não tenha sido atribuída a ninguém.

Deixe um comentário na issue dizendo que tem interesse em trabalhar. Em seguida, alguém do time vai atribuir a issue a você.

Sinta-se à vontade para fazer qualquer pergunta na página da issue antes ou durante o processo de
desenvolvimento.

Ao começar a contribuir para o projeto, é recomendável que você pegue uma issue por vez. Isso ajuda a garantir que outras pessoas também tenham a oportunidade de colaborar e evita que recursos fiquem inativos por muito tempo.

### Primeira vez contribuindo?

Para saber como contribuir pela primeira vez, leia o arquivo [CONTRIBUTING](contributing) do projeto

[contributing]: https://github.com/PGuardini/filopedia/blob/main/CONTRIBUTING.md
[docker]: https://www.docker.com/
[filopedia-issues]: https://github.com/PGuardini/filopedia/issues
[scrapy]: https://www.scrapy.org/
[SEP-contents]: https://plato.stanford.edu/contents.html
[spiders-scrapy]: https://docs.scrapy.org/en/latest/topics/spiders.html
[venv]: https://docs.python.org/3/library/venv.html
