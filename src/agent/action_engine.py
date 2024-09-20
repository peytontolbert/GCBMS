from typing import Dict
from src.agent.code_modifier import CodeModifier
from src.agent.error_handler import ErrorHandler
from src.agent.chat_with_ollama import ChatGPT
from src.agent.thought_logger import ThoughtLogger  # Import ThoughtLogger

class ActionEngine:
    def __init__(self):
        self.code_modifier = CodeModifier()
        self.error_handler = ErrorHandler()
        self.llm_client = ChatGPT()
        self.thought_logger = ThoughtLogger()  # Initialize ThoughtLogger

    async def decide_action(self, parsed_input: Dict) -> str:
        """
        Decides which action to take based on the parsed input.
        """
        action = parsed_input.get("intent", "unknown")
        self.thought_logger.log_thought(f"Decided action: {action}")  # Log decision
        return action

    async def extract_parameters(self, parsed_input: Dict) -> Dict:
        """
        Extracts parameters required for the action.
        """
        parameters = parsed_input.get("entities", {})
        self.thought_logger.log_thought(f"Extracted parameters: {parameters}")  # Log parameters
        return parameters

    async def execute_action(self, action: str, parameters: Dict) -> Dict:
        """
        Executes the determined action with the given parameters.
        """
        try:
            if action == "generate_code":
                module = parameters.get("module", "default")
                # Utilize LLM for generating code based on module
                prompt = f"Generate a Python module named '{module}' with basic structure."
                code = await self.llm_client.generate(prompt)
                updated_node = self.code_modifier.modify_code(node_id=f"{module}_module", new_content=code)
                self.thought_logger.log_thought(f"Generated code for module: {module}")  # Log code generation
                return {"action": action, "code": updated_node["content"]}
            elif action == "refactor_code":
                # Placeholder for refactoring logic
                refactored_code = "# Refactored code"
                self.thought_logger.log_thought("Refactored code")  # Log refactoring
                return {"action": action, "refactored_code": refactored_code}
            else:
                self.thought_logger.log_thought("Unknown action")  # Log unknown action
                return {"action": "unknown"}
        except Exception as e:
            error_details = self.error_handler.handle_error(e)
            self.thought_logger.log_thought(f"Error occurred: {error_details}")  # Log error
            return {"action": "error", "details": error_details}