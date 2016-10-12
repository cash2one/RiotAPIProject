URL = {
    'base': 'https://{proxy}.api.pvp.net/{url}',
    'summoner_by_name':'/api/lol/{region}/v{version}/summoner/by-name/{names}',
    'current_game':'/observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'global': '/api/lol/static-data/oce/v1.2/champion',
    'current_rank': 'api/lol/{region}/v{version}/league/by-summoner/{summonerId}/entry/'
}

API_VERSIONS = {
    'summoner': '1.4',
    'current_game': '1.0',
    'current_rank': '2.5'
}

REGIONS = {
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'oceanic': 'oce',
    'north_america': 'na',
    'global': 'global'
}

PLATFORM = {
    'eune': 'EUN1',
    'euw': 'EUW1',
    'oce': 'OC1',
    'na': 'NA1'
}