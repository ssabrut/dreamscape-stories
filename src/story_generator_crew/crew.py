from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class StoryGeneratorCrew():
    """ Story Generator Crew """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> ChatGroq:
        self.llm = ChatGroq(temperature=0, model="mixtral-8x7b-32768")

    @agent
    def input_aggregator_agent(self) -> Agent:
        return Agent(config=self.agents_config['input_aggregator_agent'], llm=self.llm)

    @task
    def input_aggregator_task(self) -> Task:
        return Task(config=self.tasks_config['input_aggregator_task'], agent=self.input_aggregator_agent())

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )