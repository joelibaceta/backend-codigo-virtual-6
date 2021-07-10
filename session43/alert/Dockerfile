FROM ubuntu:20.10

RUN apt update
RUN apt install python3 -y
RUN apt install pip -y

WORKDIR /home/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]