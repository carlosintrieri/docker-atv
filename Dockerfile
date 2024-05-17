# Usar uma imagem base oficial do Python
FROM python:3.9

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação para o diretório de trabalho
COPY . .

# Expor a porta em que a aplicação Flask será executada
EXPOSE 5000

# Definir a variável de ambiente para informar ao Flask que está em modo de produção
ENV FLASK_ENV=production

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]

