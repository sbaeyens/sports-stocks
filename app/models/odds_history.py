from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import validates

class Odds_History(db.Model):
    __tablename__ = 'odds_histories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    odds = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


    ## Relationships ##
    team = db.relationship('Team', back_populates='odds_histories')


    def to_dict(self):
        return {
            'id': self.id,
            'team_id': self.team_id,
            'odds': self.odds,
            'price': self.price,
            'date': self.date,
        }
