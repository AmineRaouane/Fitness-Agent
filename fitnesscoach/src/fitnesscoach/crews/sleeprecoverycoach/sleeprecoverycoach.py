from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv
load_dotenv()

@CrewBase
class SleepRecoveryCrew():
    """Sleeprecoverycoach crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def rest_day_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['rest_day_optimizer'],
            verbose=True
        )

    @agent
    def sleep_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['sleep_coach'],
            verbose=True
        )

    @agent
    def warmup_and_recovery_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['warmup_and_recovery_coach'],
            verbose=True
        )

    @task
    def Sleep_task(self) -> Task:
        return Task(
            config=self.tasks_config['Sleep_task']
        )

    @task
    def Rest_day_task(self) -> Task:
        return Task(
            config=self.tasks_config['Rest_day_task']
        )

    @task
    def Warmup_and_recovery_task(self) -> Task:
        return Task(
            config=self.tasks_config['Warmup_and_recovery_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
