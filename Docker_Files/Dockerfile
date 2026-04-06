FROM  python:3.13-slim-bookworm

RUN mkdir /app

COPY DS-project-1/ /app

WORKDIR /app   

RUN apt-get update -y && apt-get upgrade -y && apt-get install python3-pip -y


RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["uvicon","backend:app","--host","0.0.0.0,"--port","8080"]