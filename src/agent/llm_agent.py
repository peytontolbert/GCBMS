import logging
from typing import Dict, Any
from src.agent.nlp_processor import NLPProcessor
from src.agent.action_engine import ActionEngine
from src.agent.error_handler import ErrorHandler
from src.agent.thought_logger import ThoughtLogger
from src.agent.chat_with_ollama import ChatGPT

class LLMAgent:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.action_engine = ActionEngine()
        self.error_handler = ErrorHandler()
        self.thought_logger = ThoughtLogger()
        self.llm_client = ChatGPT()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    async def handle_user_message(self, user_message: str) -> str:
        try:
            self.logger.info("Received user message.")
            parsed_input = await self.nlp_processor.parse_input(user_message)
            self.thought_logger.log_thought(f"Parsed input: {parsed_input}")

            action = await self.action_engine.decide_action(parsed_input)
            self.thought_logger.log_thought(f"Decided action: {action}")

            parameters = await self.action_engine.extract_parameters(parsed_input)
            self.thought_logger.log_thought(f"Action parameters: {parameters}")

            result = await self.action_engine.execute_action(action, parameters)
            self.thought_logger.log_thought(f"Action result: {result}")

            response = self.generate_response(result)
            self.logger.info("Response generated successfully.")
            return response

        except Exception as e:
            self.thought_logger.log_thought(f"Error encountered: {str(e)}")
            error_response = self.error_handler.generate_error_response(e)
            return error_response

    def generate_response(self, result: Dict[str, Any]) -> str:
        if result.get("action") == "generate_code":
            code = result.get("code")
            return f"Here is the generated code:\n```python\n{code}\n```"
        elif result.get("action") == "refactor_code":
            refactored_code = result.get("refactored_code")
            return f"The code has been refactored successfully:\n```python\n{refactored_code}\n```"
        else:
            return "Action completed successfully."

