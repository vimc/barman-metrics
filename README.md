# barman-metrics
Metrics exporter for barman 

A small Flask app, designed to be run inside a docker container, that exposes a single `/metrics` endpoint returning
 metadata from the local barman instance in a format that Prometheus can use for monitoring.

Start by running:

```
sudo -H pip3 install -r requirements.txt
./run
```
