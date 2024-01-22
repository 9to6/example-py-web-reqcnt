FROM python:3.11-slim

WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD main.py main.py

CMD ["python", "main.py"]
