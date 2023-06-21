from flask import Blueprint, jsonify, session, request
from app.models import db, Odds_History
from datetime import datetime
from flask_login import current_user
# from ..utils import to_dict_list, form_errors_obj_list, print_data

odds_history_routes = Blueprint('odds_history', __name__)
