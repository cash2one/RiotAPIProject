from FlaskApp.RiotAPI import *
from FlaskApp.championid import championid


def get_summoner_id(summoner_name, api):
    summoner_data = api.get_summoner_by_name(summoner_name)
    name_formatted = summoner_name.replace(" ", "")
    summoner_id = summoner_data[name_formatted.lower()]['id']
    return summoner_id


def current_game_data(summoner_name, region, api):
    summoner_id = get_summoner_id(summoner_name, api)
    current_game = api.current_game(summoner_id, region)
    players = {}
    for player in current_game['participants']:
        players[player['summonerName']] = player.copy()
    team1_players = []
    team2_players = []
    for player in players:
        temp = [player, championid[players[player]['championId']]]
        if players[player]['teamId'] == 100:
            team1_players.append(temp)
        else:
            team2_players.append(temp)
    return team1_players, team2_players


def find_current_rank(summoner_name, api):
    summoner_id = get_summoner_id(summoner_name, api)
    current_rank = api.get_current_rank(summoner_id)
    name = current_rank[str(summoner_id)][0]['entries'][0]['playerOrTeamName']
    tier = current_rank[str(summoner_id)][0]['tier']
    lp = current_rank[str(summoner_id)][0]['entries'][0]['leaguePoints']
    playstyle = current_rank[str(summoner_id)][0]['entries'][0]['playstyle']
    division = current_rank[str(summoner_id)][0]['entries'][0]['division']
    rank = "{} {} {}LP".format(tier, division, lp)
    return [name, rank, playstyle]
