from riotwatcher import RiotWatcher
from src.application import Application


class RiotClient(object):
    _app: Application
    _watcher: RiotWatcher

    def __init__(self, app: Application):
        self._app = app
        self._watcher = RiotWatcher(app.config.riot_dev_api_key)

    @property
    def watcher(self):
        return self._watcher
