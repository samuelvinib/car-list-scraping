# Teste Prático - Listagem de Veículos (Web Scraping)

Desenvolvimento de um web scraping para buscar 10 veículos aleatórios no site da [FIPE](https://veiculos.fipe.org.br/) e armazená-los em um banco de dados MySQL.

## Tecnologias utilizadas no projeto:
- Web-scraping: Python;

## Instalação do projeto

Para rodar este projeto em sua máquina, é necessário ter o Python 3 e o pip instalados.

### Conexão com banco de dados:

Para que o web-scraping funcione e salve os dados corretamente, é necessário buildar o [Projeto Base](https://github.com/samuelvinib/car-list) primeiro, que já possui uma imagem de banco de dados MySQL com todos os parâmetros corretos para esta aplicação.

## Passo 1

Após clonar o projeto em sua máquina, navegue até o diretório raiz do projeto:

```bash
cd car-list-scraping
```

## Passo 2

Execute o seguinte comando para instalar as dependencias do projeto:

```bash
  pip install -r requirements.txt
```

## Passo 3

Após o build acesse o container da Api:

   ```bash
  python3 app.py
  ```
<br>

## Pronto!

### o python já está realizando o web scraping e salvando os dados no banco de dados!
