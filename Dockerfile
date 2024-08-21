FROM python:3.12-alpine
WORKDIR /bot
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "./main.py"]