from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,YoutubeVideoSearchTool,PDFSearchTool
from tools.tools import MusclesAvailableTool,ExercicesMakerTool,MotivationalQuotesTool
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


@CrewBase
class TrainingCrew():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def training_plan_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['training_plan_maker'],
			verbose=True,
            tools = [
                MusclesAvailableTool(),
                ExercicesMakerTool(),
                *(PDFSearchTool(
                    pdf=str(pdf_file),
                    config=dict(
                        llm=dict(
                            provider="groq",
                            config=dict(
                                model="llama-3.1-70b-versatile",
                            ),
                        ),
                        embedder=dict(
                            provider="groq",
                            config=dict(
                                model="llama-3.1-8b-instant"
                            ),
                        ),
                    )
                ) for pdf_file in list(Path("PDF").glob("*.pdf")))
            ] #YoutubeVideoSearchTool()
		)

	@agent
	def motivation_mentor(self) -> Agent:
		return Agent(
			config=self.agents_config['motivation_mentor'],
			verbose=True,
            tools=[SerperDevTool(),ScrapeWebsiteTool(),MotivationalQuotesTool()]
		)
    #?----------------------------------------------------------------
	@task
	def Planner_task(self) -> Task:
		return Task(
			config=self.tasks_config['Planner_task']
		)
	@task
	def Motivation_task(self) -> Task:
		return Task(
			config=self.tasks_config['Motivation_task']
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical,
            # manager_llm=ChatGroq(model='llama-3.1-70b-versatile')
		)
