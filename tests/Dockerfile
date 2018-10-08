FROM python:3

WORKDIR /tests

COPY ./requirements-dev.txt .
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-dev.txt

COPY ./app /app
COPY ./montagu_metrics /montagu_metrics
COPY ./tests /tests

ENTRYPOINT ["pytest", "--teamcity"]
