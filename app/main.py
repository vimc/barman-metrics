#!/usr/bin/env python3
import json
from datetime import datetime
from flask import Flask

from montagu_metrics.metrics import label_metrics, render_metrics, parse_timestamp, seconds_elapsed_since

app = Flask(__name__)

config_path = "/etc/cm/config.json"
cache_path = "/app/cache"

def get_labels():
    with open(config_path) as json_data:
        d = json.load(json_data)
        labels = d["labels"]
    return labels


def get_status():
    with open(cache_path, "r") as f:
        status = f.read()
    return status


def output_as_dict(text):
    lines = text.split("\n")
    raw_values = {}
    for line in lines:
        if line:
            print(line, flush=True)
            k, v = line.split(": ", 1)
            raw_values[k.strip()] = v.strip()
    return raw_values


def parse_status(status):
    status_values = output_as_dict(status)

    metrics_created_at = float(status_values["metrics_created_at"])
    since_last_backup = seconds_elapsed_since(metrics_created_at)

    if since_last_backup > 60 * 10:
        return {"responding": False}
    else:
        return status_values


@app.route('/metrics')
def metrics():
    try:
        status = get_status()
        ms = parse_status(status)
    except:
        ms = {"responding": False}
    labels = get_labels()
    ms = label_metrics(ms, labels)
    return render_metrics(ms)
