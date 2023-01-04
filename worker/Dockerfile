FROM python

WORKDIR ./worker

COPY . .

RUN pip install redis

CMD [ "python", "worker.py" ]