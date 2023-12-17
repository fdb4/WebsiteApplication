from app import api
from flask_restx import Resource, fields
from service.getDeactivatedWorkoutsService import getDeactivatedWorkouts

workout_bank_model=api.model(
    "Workout_Bank_Model",
    {
        "workoutID":fields.Integer(),
        "workoutname":fields.String(45),
        "videolink":fields.String(65535),
        "description":fields.String(65535),
        "musclegroup":fields.String(45),
        "equipment":fields.String(45)

    }

)

@api.route('/workouts/deactivated')
class getWorkoutsRescource(Resource):
    @api.marshal_list_with(workout_bank_model)
    def get(self):
        """Get all deactivated workouts"""
        return getDeactivatedWorkouts()