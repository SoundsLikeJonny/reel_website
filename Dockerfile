FROM python:3-alpine

WORKDIR /app

RUN apk update
RUN apk add git
RUN apk add cargo

#COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt

COPY . .
#ADD assets assets

EXPOSE 8080

CMD ["flet", "run", "./main.py"]