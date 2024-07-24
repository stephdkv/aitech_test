import json

class Config:
    def __init__(self, config_file='settings.json'):
        with open(config_file) as f:
            settings = json.load(f)
        self.repository_type = settings.get('repository', 'memory')
