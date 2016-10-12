import FlaskApp.Consts as Consts
import requests
#=Consts.REGIONS['oceanic']
#Consts.PLATFORM[self.region]


class RiotAPI():
    """Creates and formats requests to RIOT's API"""
    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params=None):
        """Sends a request"""
        if params is None:
            params = {}
        args = {'api_key': self.api_key}
        for key in params.items():
            if (key[0], key[1]) not in args.items():
                args[key[0]] = key[1]
        responce = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                url=api_url),
            params=args
        )
        return responce.json() #returns the data in JSON format

    def get_summoner_by_name(self, name):
        """Gets the summoner ID"""
        api_url = Consts.URL['summoner_by_name'].format(
            region=self.region,
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )
        return self._request(api_url)

    def current_game(self, summoner_id, region):
        """Shows Current Game Info"""
        api_url = Consts.URL['current_game'].format(
            platformId=Consts.PLATFORM[region],
            summonerId=summoner_id
            )
        return self._request(api_url)

    def champion_data(self):
        "Gets Champion IDS"
        api_url = Consts.URL['global']
        return self._request(api_url, {'champData': 'tags'})

    def get_current_rank(self, summoner_id):
        """Gets Current Rank"""
        api_url = Consts.URL['current_rank'].format(
            region=self.region,
            version=Consts.API_VERSIONS['current_rank'],
            summonerId=summoner_id
            )
        return self._request(api_url)
