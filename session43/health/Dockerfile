FROM ubuntu:20.04

RUN apt install python3 -y
RUN apt install pip

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app.py ./
COPY config.json ./

CMD ["python3", "app.py"]