import re
from typing import Dict
from src.agent.chat_with_ollama import ChatGPT  # {{ edit_1 }}
import json
class NLPProcessor:
    def __init__(self):
        self.llm_client = ChatGPT()  # {{ edit_2 }}

    async def parse_input(self, user_message: str) -> Dict:
        """
        Parses the user's message to identify intent and extract entities using LLM.
        """
        prompt = (
            "Analyze the following user message and return a JSON object with 'intent' and 'entities'.\n\n"
            f"User Message: {user_message}"
        )
        response = await self.llm_client.generate(prompt)  # {{ edit_3 }}
        # Assuming the LLM returns a JSON string
        try:
            parsed = json.loads(response)
            return parsed
        except json.JSONDecodeError:
            return {"intent": "unknown", "entities": {}}

    def generate_response(self, parsed_input: Dict) -> str:
        """
        Generates a response based on the parsed input.
        """
        intent = parsed_input.get("intent")
        if intent == "generate_code":
            module = parsed_input["entities"].get("module", "module")
            return f"Generating code for the new {module} module."
        return "I'm not sure how to help with that."