import os
import abc


class BaseConfig(object, metaclass=abc.ABCMeta):

    def __init__(self, **kwargs):
        for param, value in kwargs.items():
            setattr(self, '_{}'.format(param), value)


class AppConfig(BaseConfig):
    _riot_dev_api_key = os.environ.get('RIOT_DEV_API_KEY')
    _riot_dev_api_region = os.environ.get('RIOT_DEV_API_REGION')

    @property
    def riot_dev_api_region(self):
        return self._riot_dev_api_region

    @property
    def riot_dev_api_key(self):
        return self._riot_dev_api_key
