import json
from montagu_metrics.metrics import seconds_elapsed_since


def get_status(cache_file_location):
    with open(cache_file_location, "r") as f:
        status = json.load(f)
    return status


def parse_status(status, max_age_seconds):
    print(status)
    metrics_created_at = float(status["utc_seconds"])
    since_last_backup = seconds_elapsed_since(metrics_created_at)

    if since_last_backup > max_age_seconds:
        return {"cache_out_of_date": True}
    else:
        data = status["data"]
        data.update({"cache_out_of_date": False})
        return data
