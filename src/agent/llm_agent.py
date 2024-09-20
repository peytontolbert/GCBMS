import logging
from typing import Dict, Any
from src.llm_agent.nlp_processor import NLPProcessor
from src.llm_agent.action_engine import ActionEngine
from src.llm_agent.code_modifier import CodeModifier
from src.llm_agent.error_handler import ErrorHandler
from src.llm_agent.thought_logger import ThoughtLogger
from src.llm_agent.chat_with_ollama import ChatGPT
from src.database.node_manager import NodeManager
from src.database.edge_manager import EdgeManager
from src.database.query_engine import QueryEngine

class LLMAgent:

    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.action_engine = ActionEngine()
        self.code_modifier = CodeModifier()
        self.error_handler = ErrorHandler()
        self.thought_logger = ThoughtLogger()
        self.ollama_client = ChatGPT()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)


    def handle_user_message(self, user_message: str) -> str:
        try:
            self.logger.info("Received user message.")
            parsed_input = self.nlp_processor.parse_input(user_message)
            self.thought_logger.log_thought(f"Parsed input: {parsed_input}")

            action = self.action_engine.decide_action(parsed_input)
            self.thought_logger.log_thought(f"Decided action: {action}")

            parameters = self.action_engine.extract_parameters(parsed_input)
            self.thought_logger.log_thought(f"Action parameters: {parameters}")

            result = self.action_engine.execute_action(action, parameters)
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

