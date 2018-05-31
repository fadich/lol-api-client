import os
import abc


class BaseConfig(object, metaclass=abc.ABCMeta):

    def __init__(self, **kwargs):
        for param, value in kwargs.items():
            setattr(self, '_{}'.format(param), value)


class AppConfig(BaseConfig):
    _db_host = os.environ.get('DB_HOST')
    _db_auto_connect = os.environ.get('DB_AUTO_CONNECT', True)
    _riot_dev_api_key = os.environ.get('RIOT_DEV_API_KEY')
    _riot_dev_api_region = os.environ.get('RIOT_DEV_API_REGION')

    @property
    def db_host(self):
        return self._db_host

    @property
    def db_auto_connect(self):
        return self._db_auto_connect

    @property
    def riot_dev_api_region(self):
        return self._riot_dev_api_region

    @property
    def riot_dev_api_key(self):
        return self._riot_dev_api_key
