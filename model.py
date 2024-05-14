from controller import *
from sqlalchemy import create_engine, Column, Integer, String, Float,DateTime
import datetime
from app import *

engine = create_engine('sqlite:///database.db')
Base = declarative_base()


class Game_DB(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(1000), nullable=False)
    team_1 = Column(String(200))
    team_2 = Column(String(200))
    coef_win_1 = Column(Float, nullable=False)
    coef_win_2= Column(Float, nullable=False)
    timee = Column(String(200))
    datee = Column(String(200))
    # coef_draw = Column(Float, nullable=False)
    start = Column(DateTime)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def __make_session():
    return sessionmaker(engine)()

def game_exists(name, team_1, team_2, timee, datee):
    session = __make_session()
    existing_game = session.query(Game_DB).filter_by(name=name, team_1=team_1, team_2=team_2, timee=timee, datee=datee).first()
    return existing_game is not None


def add_game(name, team_1, team_2, coef_win_1, coef_win_2, timee, datee):
    if game_exists(name, team_1, team_2,timee, datee):
        return None

    session = __make_session()
    new_game = Game_DB(
        name=name, 
        team_1=team_1, 
        team_2=team_2, 
        coef_win_1=float(coef_win_1) if coef_win_1 else 0,
        coef_win_2=float(coef_win_2) if coef_win_2 else 0,
        timee = timee,
        datee = datee,
        start=datetime.datetime.now()
    )
    session.add(new_game)
    session.commit()
    send_message_to_channel({
        "name":name, 
        "team_1":team_1, 
        "team_2":team_2, 
        "coef_win_1": coef_win_1,
        "coef_win_2": coef_win_2,
        "timee": timee,
        "datee": datee,
    })