FROM python:latest

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app ./app

# -u allows stdout to be written in docker container
CMD ["python", "-u", "main.py"]