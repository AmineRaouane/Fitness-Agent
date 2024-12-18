from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
import agentops
import os
from crews.nutritioncoach.nutritioncoach import NutritionCrew
from crews.sleeprecoverycoach.sleeprecoverycoach import SleepRecoveryCrew
from crews.trainingcoach.trainingcoach import TrainingCrew

class FitnessState(BaseModel):
    TrainingResults: str = ""
    NutritionResults: str = ""
    SleepRecoveryResults: str = ""

TrainingInputs = {
    'fitness_level':'beginner',
    'num_sessions':4,
    'fitness_goal':'muscle gain',
    'current_progress':'3 months of training',
    'challenges':'No visible results'
}
NutritionInputs = {
    'dietary_preferences':'chicken',
    'fitness_goal':'muscle gain',
    'metrics':{
    	"weight":{
            'value':80,
            'unit':'kg'
        },
    	'height':{
            'value':180,
            'unit':'cm'
        },
    	'sex': 'm',
    	'age': 22,
    	'waist': 30,
    	'hip': 40,
    }
}
SleepRecoveryInputs = {
    'current_sleep_hours':6,
    'current_sleep_quality':'moderate',
    'specific_issues':'trouble falling asleep',
    'activity_preferences':'swimming',
    'recovery_needs':'muscle soreness',
    'training_type':'strength',
    'injuries_restrictions':'None'
}

class FitnessCoachFlow(Flow[FitnessState]):

    @start()
    def generate_training_plan(self):
        print("Generating training plan")
        result = (
            TrainingCrew()
            .crew()
            .kickoff(inputs=TrainingInputs)
        )
        print("training plan generated", result.raw)
        self.state.TrainingResults = result.raw

    @listen(generate_training_plan)
    def generate_nutrition_plan(self):
        print("Generating nutrition plan")
        result = (
            NutritionCrew()
            .crew()
            .kickoff(inputs=NutritionInputs)
        )
        print("nutrition plan generated", result.raw)
        self.state.NutritionResults = result.raw

    @listen(generate_training_plan)
    def generate_sleep_plan(self):
        print("Generating Sleep plan")
        result = (
            SleepRecoveryCrew()
            .crew()
            .kickoff(inputs=SleepRecoveryInputs)
        )
        print("Sleep plan generated", result.raw)
        self.state.SleepRecoveryResults = result.raw


# def kickoff():
#     Session = agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'))
#     Fitness_flow = FitnessCoachFlow()
#     Fitness_flow.plot()
#     Fitness_flow.kickoff()
#     Session.end_session()

def kickoff():
    Session = agentops.init(api_key=os.getenv('AGENTOPS_API_KEY'))
    print("Generating training plan")
    result = (
        TrainingCrew()
        .crew()
        .kickoff(inputs=TrainingInputs)
    )
    print("training plan generated", result.raw)
    Session.end_session()

if __name__ == "__main__":
    kickoff()
