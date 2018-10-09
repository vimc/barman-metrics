# cached-metrics
Metrics exporter for Prometheus. 

A small Flask app, designed to be run inside a docker container, that exposes a single `/metrics` endpoint 
returning metadata from a local cache file in a format that Prometheus can use for monitoring. 

Clone with `--recursive` and start by running:

```
sudo -H pip3 install -r requirements.txt
sudo -H pip3 install -r ./montagu_metrics/requirements.txt
./scripts/run
```

## Tests

To run tests inside a docker container, with `config-example.json` mounted as the config file:
```
./scripts/teamcity.sh
```

To run tests locally you need to copy `config-example.json` to `/etc/cm/config.json` where the app expects to
find its config. 