FROM python:3.10
WORKDIR /bot
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "./main.py"]