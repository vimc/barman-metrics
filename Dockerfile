FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app
COPY ./requirements.txt /app
COPY ./montagu_metrics /app/montagu_metrics

RUN pip3 install -r /app/requirements.txt
RUN pip3 install -r /app/montagu_metrics/requirements.txt

ENV STATIC_INDEX 1

