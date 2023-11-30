from app import api
from flask_restx import Resource, fields
from service.getWorkoutsService import getWorkouts

workout_bank_model=api.model(
    "Workout_Bank_Model",
    {
        "workoutID":fields.Integer(),
        "workoutname":fields.String(45),
        "videolink":fields.String(65535),
        "difficulty":fields.Integer(),
        "musclegroup1":fields.String(45),
        "musclegroup2":fields.String(45),
        "musclegroup3":fields.String(45)

    }

)

@api.route('/workouts')
class getWorkoutsRescource(Resource):
    @api.marshal_list_with(workout_bank_model)
    def get(self):
        """Get all workouts"""
        return getWorkouts()