FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
COPY articles.sql /docker-entrypoint-initdb.d/

FROM python
WORKDIR /src
COPY . /src
CMD [ "python", "main.py"]

