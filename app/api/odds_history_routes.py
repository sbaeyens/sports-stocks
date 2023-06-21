from flask import Blueprint, jsonify, session, request
from app.models import db, Odds_History, Transfer, Team
from datetime import datetime
from flask_login import current_user
# from ..utils import to_dict_list, form_errors_obj_list, print_data

odds_history_routes = Blueprint('odds_history', __name__)


#get transactions by ticker
@odds_history_routes.route('/<string:league>/<string:code>')
def get_transfers(league, code):
    print("league & code \n\n\n\n", league, code)
    team = Team.query.filter(
        Team.code == code,
        Team.league == league
    ).one().to_dict()

    print("team.id \n\n\n\n\n", team['id'], "\n\n\n\n")
    team_id = team['id']

    season_odds = Odds_History.query.filter(
        Odds_History.team_id == team_id
        ).order_by(Odds_History.date)

    transfer_list = [item.to_dict() for item in list(season_odds)]

    return transfer_list
