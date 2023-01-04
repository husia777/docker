FROM python

WORKDIR ./producer

COPY . .

RUN pip install redis

CMD [ "python", "producer.py" ]