import asyncio

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types


class SimpleRunner:
    _DEFAULT_USER_ID = "user"
    _DEFAULT_APPLICATION_NAME = "agents"

    def __init__(self, user_id=None, application_name=None):
        self._user_id = user_id if user_id else SimpleRunner._DEFAULT_USER_ID
        self._application_name = application_name if application_name else SimpleRunner._DEFAULT_APPLICATION_NAME

    def run(self, agent: Agent, message: str) -> str:

        runner = InMemoryRunner(agent, app_name=self._application_name)
        
        session = asyncio.run(runner.session_service.create_session(
            app_name=self._application_name, user_id=self._user_id
        ))

        message = types.Content(
            role='user', parts=[types.Part(text=message)]
        )

        response = None
        
        for event in runner.run(user_id = self._user_id, session_id = session.id, new_message = message) :
            if event.is_final_response() :
                if (event.content.parts) and (len(event.content.parts) > 0):
                    if event.content.parts[0].text : 
                        response = event.content.parts[0].text

        return response