FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /giftme/

RUN pip install --upgrade pip
COPY reqiurements.txt /giftme/
RUN pip install -r reqiurements.txt

COPY . /giftme/