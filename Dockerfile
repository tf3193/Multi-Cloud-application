FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN mkdir -p /opt/microservices
ADD . /opt/microservices
RUN pip install -r /opt/microservices/requirements.txt

WORKDIR /opt/microservices
EXPOSE 5000

CMD python3 app.py
