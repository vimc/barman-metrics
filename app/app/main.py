#!/usr/bin/env python3
from flask import Flask, Response

from .core.settings import load_settings
from .core.metrics import get_status, parse_status
from montagu_metrics.metrics import label_metrics, render_metrics

app = Flask(__name__)

settings = load_settings()


@app.route('/metrics')
def metrics():
    try:
        status = get_status(settings.cache_file)
        ms = parse_status(status, settings.max_age_seconds)
    except:
        ms = {"responding": False}
    labels = settings.labels
    ms = label_metrics(ms, labels)
    return Response(render_metrics(ms), mimetype="text/plain")
