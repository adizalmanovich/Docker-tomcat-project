FROM python:3-alpine

MAINTAINER adi

COPY . /app_new

WORKDIR /app_new

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python", "app.py" ]
