import json
from montagu_metrics.metrics import seconds_elapsed_since


def get_status(cache_file_location):
    try:
        with open(cache_file_location, "r") as f:
            status = json.load(f)
        return status
    except:
        return


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
