from .orm import connect
from .config import AppConfig


class Application(object):
    _config: AppConfig = None

    def __init__(self, config: AppConfig):
        self._config = config

        if self.config.db_auto_connect:
            connect(self.config.db_host)

    @property
    def config(self):
        return self._config
