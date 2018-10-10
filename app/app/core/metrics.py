import json
from .settings import cache_path
from montagu_metrics.metrics import seconds_elapsed_since


def get_status():
    with open(cache_path, "r") as f:
        status = json.load(f)
    return status


def parse_status(status, max_age_seconds):
    print(status)
    metrics_created_at = float(status["utc_seconds"])
    since_last_backup = seconds_elapsed_since(metrics_created_at)

    if since_last_backup > max_age_seconds:
        return {"responding": False}
    else:
        data = status["data"]
        data.update({"responding": True})
        return data
