from src import Application, AppConfig, RiotClient

import json


if __name__ == '__main__':

    app = Application(AppConfig(
        db_auto_connect=False,
        riot_dev_api_key='RGAPI-7b60f5da-d7a9-4bfd-853e-02261aeed0b8',
        riot_dev_api_region='EUW1'
    ))

    client = RiotClient(app)

    champions = client.watcher.static_data.champions(
        region=app.config.riot_dev_api_region)
    print(json.dumps(champions, indent=4))

    items = client.watcher.static_data.items(
        region=app.config.riot_dev_api_region)
    print(json.dumps(items, indent=4))
