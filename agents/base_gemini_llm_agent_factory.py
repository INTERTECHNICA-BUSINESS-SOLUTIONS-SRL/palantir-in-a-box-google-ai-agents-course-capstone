import os

from abc import ABC, abstractmethod
from typing import List, Dict

from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini


class BaseGeminiLLMAgentFactory (ABC):
    
    def _get_retry_config(self) -> types.HttpRetryOptions:
        retry_config = types.HttpRetryOptions(
            attempts=5,
            exp_base=7,
            initial_delay=10,
            http_status_codes=[429, 500, 503, 504]
        )

        return retry_config

    def _get_baseline_llm(self) -> str:
        assert not os.environ["BASELINE_LLM"] is None
        return os.environ["BASELINE_LLM"]

    def _get_tools(self) -> List :
        return None

    def _get_output_key(self) -> List :
        return None
    
    def _get_additional_arguments(self) -> Dict[str, any]:
        return None

    @abstractmethod
    def _get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _get_instruction(self) -> str:
        raise NotImplementedError

    def get_agent(self) -> LlmAgent:
        agents_arguments = {
            "name": self._get_name(),
            "model": Gemini(
                model = self._get_baseline_llm(),
                retry_options = self._get_retry_config()
            ),
            "instruction": self._get_instruction()
        }
        
        if self._get_tools() :
            agents_arguments["tools"] = self._get_tools()
        
        if self._get_output_key() :
            agents_arguments["output_key"] = self._get_output_key()

        if self._get_additional_arguments() :
            agents_arguments.update(self._get_additional_arguments())
            
        agent = LlmAgent(**agents_arguments)
        
        return agent
