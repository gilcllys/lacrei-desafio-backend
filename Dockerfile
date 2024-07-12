# Use uma imagem base oficial do Python
FROM python:3.12-alpine

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app


#copiando todos os arquivos para a pasta de trabalho
COPY . /app

#acessando a pasta do projeto
RUN cd lacrei_backend


# Instale as dependências do Python
RUN pip install -r requirements.txt


# Copie o arquivo de variáveis de ambiente para o contêiner
COPY .env .env

# Exponha a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
