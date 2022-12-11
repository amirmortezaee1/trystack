FROM python:slim

LABEL maintainer="Amir Mortezaee <amir.mortezaee1@gmail.com>"

EXPOSE 8080/tcp

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ./start
