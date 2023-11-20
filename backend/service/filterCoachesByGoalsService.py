from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def filterCoachByGoal(goal):
    query = text(
    "select info2.clientID, info2.email, info2.firstname, info2.lastname, info2.price, info2.rating, info2.experience, info2.bio, info2.goal, info2.town, s.state "
    "from schema.state s "
    "join "
    "(select info.clientID, info.email, info.firstname, info.lastname, info.price, info.rating, info.experience, info.bio, c.goal, l.town, l.stateID "
    "from location l "
    "join( "
    "select c.clientID, c.email, c.firstname, c.lastname, x.price, x.rating, x.experience, x.bio, x.locationID, x.goal "
    "from schema.clients c "
    "join schema.coachexp x "
    "where c.coachexpid = x.coachexpid) info "
    "where info.locationID = l.locationID and info.goal = :gl) info2 "
    "where info2.stateID = s.StateID;")
    query = query.bindparams(gl=goal)

    results = db.session.execute(query).fetchall()
    return results
