FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 5001
CMD ["python3", "videos-api.py"]
