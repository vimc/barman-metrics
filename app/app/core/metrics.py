from .settings import cache_path
from montagu_metrics.metrics import seconds_elapsed_since


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


def parse_status(status, max_age_seconds):
    status_values = output_as_dict(status)
    metrics_created_at = float(status_values["metrics_created_at"])
    since_last_backup = seconds_elapsed_since(metrics_created_at)

    if since_last_backup > max_age_seconds:
        return {"responding": False}
    else:
        status_values.update({"responding": True})
        return status_values
