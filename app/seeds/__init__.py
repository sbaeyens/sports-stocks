from flask.cli import AppGroup
from .users import seed_users, undo_users
from .stocks import seed_stocks, undo_stocks
from .portfolios import seed_portfolios, undo_portfolios
from .investments import seed_investments, undo_investments
from .transactions import seed_transactions, undo_transactions
from .watchlists import seed_watchlists, undo_watchlists
from .watchlist_stocks import seed_watchlist_stocks, undo_watchlist_stocks
from .transfers import seed_transfers, undo_transfers
from .odds_history import seed_odds_history, undo_odds_history
from .teams import seed_teams, undo_teams
# from .portfolio_history import seed_portfolio_history, undo_portfolio_history

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_transfers()
        undo_watchlist_stocks()
        undo_watchlists()
        undo_transactions()
        undo_investments()
        # undo_portfolio_history()
        undo_odds_history()
        undo_teams()
        undo_portfolios()
        undo_stocks()
        undo_users()
    seed_users()
    seed_stocks()
    seed_portfolios()
    # seed_portfolio_history()
    seed_odds_history()
    seed_teams()
    seed_investments()
    seed_transactions()
    seed_watchlists()
    seed_watchlist_stocks()
    seed_transfers()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_transfers()
    undo_watchlist_stocks()
    undo_watchlists()
    undo_transactions()
    undo_investments()
    # undo_portfolio_history()
    undo_odds_history()
    undo_teams()
    undo_portfolios()
    undo_stocks()
    undo_users()
    # Add other undo functions here
