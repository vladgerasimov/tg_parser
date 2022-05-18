FROM python:latest

COPY ./app ./app

WORKDIR /app

RUN pip install -r requirements.txt

# -u allows stdout to be written in docker container
CMD ["python", "-u", "main.py"]