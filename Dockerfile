FROM python:3.10
WORKDIR /bot
COPY requirements.txt .
RUN pip3 install -r requirements.txt
# This thing below essentialy makes all the tokens hardcoded and unchangable without container rebuild... TODO: Change
COPY . .
CMD ["python3", "./main.py"]