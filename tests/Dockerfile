FROM python:3

WORKDIR /app

COPY ./requirements-dev.txt /app/
COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-dev.txt

COPY ./bin /app/bin
COPY ./tests /app/tests

ENTRYPOINT ["pytest", "--teamcity"]
