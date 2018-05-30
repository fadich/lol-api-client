from src.config import AppConfig


class Application(object):
    _config: AppConfig = None

    def __init__(self, config: AppConfig):
        self._config = config

    @property
    def config(self):
        return self._config
