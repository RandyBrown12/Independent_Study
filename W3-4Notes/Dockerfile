FROM python:3.10-slim

WORKDIR /app

COPY flaskweb.py .

RUN pip install flask && apt-get update && apt-get install -y curl

EXPOSE 5000

CMD ["flask", "--app", "flaskweb", "run", "--host=0.0.0.0", "--port=5000"]