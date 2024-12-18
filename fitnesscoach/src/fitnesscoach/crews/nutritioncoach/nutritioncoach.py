from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,YoutubeVideoSearchTool

from tools.tools import BMICalculatorTool

from dotenv import load_dotenv
load_dotenv()

@CrewBase
class NutritionCrew():
	"""Nutritioncoach crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def nutrition_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['nutrition_specialist'],
			verbose=True,
            tools=[BMICalculatorTool(),SerperDevTool(),ScrapeWebsiteTool()] #
		)

	@task
	def Nutrition_task(self) -> Task:
		return Task(
			config=self.tasks_config['Nutrition_task']
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)
