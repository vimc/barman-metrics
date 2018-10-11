import json
import os

config_path = "/etc/cm/config.json"
cache_path = "/app/cache"


class Settings:
    def __init__(self, path=config_path):
        with open(path, 'r') as f:
            config = json.load(f)

        self.labels = config["labels"]
        self.cache_file = os.path.join(cache_path, config["cache_filename"])
        self.max_age_seconds = config["max_age_seconds"]


def load_settings():
    return Settings()
