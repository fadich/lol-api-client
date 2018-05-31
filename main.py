from src import Application, AppConfig, RiotClient

import json


if __name__ == '__main__':

    app = Application(AppConfig(
        db_host='mongodb://localhost:27017/lol_static',
        riot_dev_api_key='RGAPI-793ea4dc-df01-4189-9104-b8b497c586ae',
        riot_dev_api_region='EUW1'
    ))

    client = RiotClient(app)

    champions = client.watcher.static_data.champions(
        region=app.config.riot_dev_api_region)
    print(json.dumps(champions, indent=4))

    items = client.watcher.static_data.items(
        region=app.config.riot_dev_api_region)
    print(json.dumps(items, indent=4))
