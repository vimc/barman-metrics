# cached-metrics
Metrics exporter for Prometheus. 

A small Flask app, designed to be run inside a docker container, that exposes a single `/metrics` endpoint 
returning metadata from a local cache file in a format that Prometheus can use for monitoring. 

To get a minimal example working locally:

1. Clone with `--recursive`
2. Create a file called `metrics.json` in the root of this directory by copying `cache-example`
3. Create a file called `config.json` in the root of this directory by copying `config-example.json` 
and changing the `cache_volume` property to the absolute path of this directory
4. Start the app by running:
    ```
    sudo -H pip3 install -r requirements.txt
    sudo -H pip3 install -r ./montagu_metrics/requirements.txt
    ./scripts/run
    ```
5. To see the metrics change, change the `utc_seconds` value in `metrics.json` to a a value less
than 5 minutes ago (convert current time to seconds here https://www.epochconverter.com/)

## Config

See `config-example.json` in this directory for an example config.

```
{
  "labels": {
    "db_name": "montagu"
  },
  "cache_volume": "barman_metrics",
  "cache_filename": "metrics.json",
  "port": 5000,
  "name": "barman-metrics",
  "max_age_seconds": 600
}
```

* `labels` are used by Prometheus to group metrics, and can be anything you like (see https://prometheus.io/docs/practices/naming/)
* `cache_volume` can be a named volume or absolute path, and is where the cache file will be found
* `cache_filename` is the name of the cache file
* `port` is the port the app will run on
* `name` is the name of the container the app will run as
* `max_age_seconds` is the threshold at which the app will consider cached data stale

## Tests

To run tests inside a docker container, with `config-example.json` mounted as the config file:
```
./scripts/test.sh
```

To run tests not inside docker you would need to copy `config-example.json` to `/etc/cm/config.json` where the 
app expects to find its config, and `cache-example` to `/app/cache/metrics.json` where the app expects the cache file.

## Teamcity

On Teamcity the script `./scripts/teamcity.sh` is run, which runs tests and pushes the container to 
the montagu registry. To build the container locally, run
```
docker build \
       --tag $APP_DOCKER_COMMIT_TAG \
       --tag $APP_DOCKER_BRANCH_TAG \
       .
```