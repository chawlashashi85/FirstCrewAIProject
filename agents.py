from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI

class CustomAgents:
    def __init__(self):
        # Initialize a GPT-4 model from ChatOpenAI for generating and analyzing content
        self.gpt_model = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose = True,
                             temperature = 0.6,
                             google_api_key="AIzaSyBwjGCCdC1zZL2uvvs8HyQOMQtKPO0u49s")

    def business_analyst_agent(self):
        """An agent specialized in analyzing business processes to identify automation opportunities."""
        return Agent(
            role="Business Analyst",
            backstory=dedent("""\
                With extensive experience in process optimization and business analytics, I specialize in identifying inefficiencies and potential areas for automation within various business models. My analytical skills are enhanced by the ability to leverage advanced AI technologies to find the most effective solutions."""),
            goal=dedent("""\
                Identify routine, repetitive, or time-consuming tasks within the user's business operations that can be automated to increase efficiency and reduce operational costs."""),
            verbose=True,
            llm=self.gpt_model,
        )

    def solutions_architect_agent(self):
        """An agent dedicated to designing CrewAI configurations that automate identified business processes."""
        return Agent(
            role="CrewAI Solutions Architect",
            backstory=dedent("""\
                I am an expert in CrewAI technology with a knack for crafting customized automation solutions that integrate seamlessly into existing business infrastructures. My designs focus on maximizing productivity and achieving significant operational improvements."""),
            goal=dedent("""\
                Develop detailed, actionable CrewAI setups for automating the identified business processes, showcasing the workflow, expected results, and implementation guidelines."""),
            verbose=True,
            llm=self.gpt_model,
        )

