#!/usr/bin/env python3
from flask import Flask

from .core.settings import load_settings
from .core.metrics import get_status, parse_status
from montagu_metrics.metrics import label_metrics, render_metrics

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    try:
        status = get_status()
        ms = parse_status(status)
    except:
        ms = {"responding": False}
    labels = load_settings().labels
    ms = label_metrics(ms, labels)
    return render_metrics(ms)