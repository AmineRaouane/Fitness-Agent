from crewai.tools import BaseTool
from pydantic import BaseModel, Field, conint, confloat
from typing import Literal, Type
import requests
from agentops import record_tool
from tools.nutrition_tool import calculate_BMI
from tools.training_tool import fetch_muscles,exercises_for_muscle,motivational_quotes

#?-------------------------------Tool1------------------------------
class BMICalculatorModel(BaseModel):
    weight_value: confloat(ge=0)
    weight_unit: Literal["kg", "cm", "m", "lb", "in"]
    height_value: confloat(ge=0)
    height_unit: Literal["kg", "cm", "m", "lb", "in"]
    sex: Literal["m", "f"]
    age: conint(ge=0)
    waist: confloat(ge=0)
    hip: confloat(ge=0)

@record_tool('BMICalculatorTool')
class BMICalculatorTool(BaseTool):
    name: str = "BMI Calculator"
    description: str = (
        "This tool is usefull when you want to calculate the BMI for someone based on some metrics"
    )
    args_schema: Type[BaseModel] = BMICalculatorModel

    def _run(self,weight_value,weight_unit,height_value,height_unit,sex,age,waist,hip) :
        try :
            return calculate_BMI(weight_value,weight_unit,height_value,height_unit,sex,age,waist,hip)
        except :
            return "An error has occured while calculating the BMI"

#?-------------------------------Tool2------------------------------
class ExercicesMakerModel(BaseModel):
    Muscle_name : str = Field(description="The muscle you want to get exercices for")

@record_tool('ExercicesMakerTool')
class ExercicesMakerTool(BaseTool):
    name: str = "Exercices maker"
    description: str = (
        "This tool is usefull when you want to get exercices for a specific muscle"
    )
    args_schema: Type[BaseModel] = ExercicesMakerModel

    def _run(self, muscle_name) -> str:
        try :
            return exercises_for_muscle(muscle_name)
        except :
            return "An error has occured while getting the exercices"
#!-------------------------------SubTool------------------------------
@record_tool('MusclesAvailableTool')
class MusclesAvailableTool(BaseTool):
    name: str = "Muscles available"
    description: str = (
        "This tool is usefull when you want to know the available muscles that you acn give to the Exercices maker tool"
    )

    def _run(self) -> str:
        try :
            return fetch_muscles()
        except :
            return "An error has occured while getting the muscles"

#?-------------------------------Tool3------------------------------
@record_tool('MotivationalQuotesTool')
class MotivationalQuotesTool(BaseTool):
    name: str = "Motivational quotes generator"
    description: str = (
        "This tool is usefull when you want to get some motivational quotes"
    )

    def _run(self) -> str:
        try :
            return motivational_quotes()
        except :
            return "An error has occured while getting the motivational quotes"
