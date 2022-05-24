FROM python:3.9
WORKDIR /app
# test
COPY requirements.txt .
RUN pip3 install --no-cache-dir --default-timeout=30 -r requirements.txt
COPY . /app
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]

