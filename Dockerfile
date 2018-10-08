FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./requirements.txt .
COPY ./app/montagu_metrics/requirements.txt ./app/montagu_metrics/
RUN pip3 install -r requirements.txt
RUN pip3 install -r ./app/montagu_metrics/requirements.txt

ENV STATIC_INDEX 1
COPY app /app
