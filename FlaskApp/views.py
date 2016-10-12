from flask import Flask, render_template, request, jsonify
from FlaskApp import app
from .apiFunctions import *
app.debug = True


@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/header')
def header():
    return render_template("header.html")

@app.route('/current')
def current():
    return render_template("current.html")


@app.route('/currentgame', methods=['POST'])
def current_game_output():
    region = request.form['region']
    summoner_name = request.form['summoner_name']
    api = RiotAPI('ddf7175a-c715-4fd8-be9c-95b85b49dd90', region)
    team1, team2 = current_game_data(summoner_name, region, api)
    return render_template("output.html",team1=team1,team2=team2)


@app.route('/rank')
def rank():
    return render_template("rank.html")


@app.route('/rank', methods=['GET', 'POST'])
def current_rank():
    region = request.form['region']
    api = RiotAPI('ddf7175a-c715-4fd8-be9c-95b85b49dd90', region)
    summoner_name = request.form['summoner_name']
    rank_data = find_current_rank(summoner_name, api)
    return render_template("rank.html",player=rank_data)
