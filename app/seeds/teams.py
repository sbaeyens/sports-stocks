from app.models import db, Team, environment, SCHEMA
from sqlalchemy.sql import text


def seed_teams():
    teams = [
        {'code':"ATL",'name':"Atlanta Hawks",'league':"NBA"},
        {'code':"BOS",'name':"Boston Celtics",'league':"NBA"},
        {'code':"BKN",'name':"Brooklyn Nets",'league':"NBA"},
        {'code':"CHA",'name':"Charlotte Hornets",'league':"NBA"},
        {'code':"CHI",'name':"Chicago Bulls",'league':"NBA"},
        {'code':"CLE",'name':"Cleveland Cavaliers",'league':"NBA"},
        {'code':"DAL",'name':"Dallas Mavericks",'league':"NBA"},
        {'code':"DEN",'name':"Denver Nuggets",'league':"NBA"},
        {'code':"DET",'name':"Detroit Pistons",'league':"NBA"},
        {'code':"GSW",'name':"Golden State Warriors",'league':"NBA"},
        {'code':"HOU",'name':"Houston Rockets",'league':"NBA"},
        {'code':"IND",'name':"Indiana Pacers",'league':"NBA"},
        {'code':"LAC",'name':"Los Angeles Clippers",'league':"NBA"},
        {'code':"LAL",'name':"Los Angeles Lakers",'league':"NBA"},
        {'code':"MEM",'name':"Memphis Grizzlies",'league':"NBA"},
        {'code':"MIA",'name':"Miami Heat",'league':"NBA"},
        {'code':"MIL",'name':"Milwaukee Bucks",'league':"NBA"},
        {'code':"MIN",'name':"Minnesota Timberwolves",'league':"NBA"},
        {'code':"NOP",'name':"New Orleans Pelicans",'league':"NBA"},
        {'code':"NYK",'name':"New York Knicks",'league':"NBA"},
        {'code':"OKC",'name':"Oklahoma City Thunder",'league':"NBA"},
        {'code':"ORL",'name':"Orlando Magic",'league':"NBA"},
        {'code':"PHI",'name':"Philadelphia 76ers",'league':"NBA"},
        {'code':"PHX",'name':"Phoenix Suns",'league':"NBA"},
        {'code':"POR",'name':"Portland Trail Blazers",'league':"NBA"},
        {'code':"SAC",'name':"Sacramento Kings",'league':"NBA"},
        {'code':"SAS",'name':"San Antonio Spurs",'league':"NBA"},
        {'code':"TOR",'name':"Toronto Raptors",'league':"NBA"},
        {'code':"UTA",'name':"Utah Jazz",'league':"NBA"},
        {'code':"WAS",'name':"Washington Wizards",'league':"NBA"},
    ]

    for team in teams:
        db.session.add(Team(
            code=team['code'],
            name=team['name'],
            league=team['league'],
        ))

    db.session.commit()


## unseed function
def undo_teams():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teams RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teams"))

    db.session.commit()
