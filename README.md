# barman-metrics
Metrics exporter for barman 

A small Flask app, designed to be run inside a docker container, that exposes a single `/metrics` endpoint returning
 metadata from the local barman instance in a format that Prometheus can use for monitoring.

Clone with `--recursive` and start by running:

```
sudo -H pip3 install -r requirements.txt
sudo -H pip3 install -r ./montagu_metrics/requirements.txt
./scripts/run
```

## Tests
To run tests

```
sudo -H pip3 install -r requirements-dev.txt
pytest
```

or to run in a docker container
```
./scripts/teamcity.sh
```