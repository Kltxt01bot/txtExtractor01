FROM python:3.8.1-slim-buster

WORKDIR .
COPY . .

RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]
