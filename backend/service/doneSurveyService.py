from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def doneSurvey(clientID):
    query = text(
        "select * from clients where clientID = :cid"
    )

    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).first()
    if results.geninfoID == None and results.workoutgoalID == None:
        return {"survey": 1}
    else:
        return {"survey": 0}
