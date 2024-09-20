from typing import Dict
from src.agent.code_modifier import CodeModifier
from src.agent.error_handler import ErrorHandler
from src.agent.chat_with_ollama import ChatGPT

class ActionEngine:
    def __init__(self):
        self.code_modifier = CodeModifier()
        self.error_handler = ErrorHandler()
        self.llm_client = ChatGPT()

    async def decide_action(self, parsed_input: Dict) -> str:
        """
        Decides which action to take based on the parsed input.
        """
        return parsed_input.get("intent", "unknown")

    async def extract_parameters(self, parsed_input: Dict) -> Dict:
        """
        Extracts parameters required for the action.
        """
        return parsed_input.get("entities", {})

    async def execute_action(self, action: str, parameters: Dict) -> Dict:
        """
        Executes the determined action with the given parameters.
        """
        if action == "generate_code":
            module = parameters.get("module", "default")
            # Utilize LLM for generating code based on module
            prompt = f"Generate a Python module named '{module}' with basic structure."
            code = await self.llm_client.generate(prompt)
            updated_node = self.code_modifier.modify_code(node_id=f"{module}_module", new_content=code)
            return {"action": action, "code": updated_node["content"]}
        elif action == "refactor_code":
            # Placeholder for refactoring logic
            refactored_code = "# Refactored code"
            return {"action": action, "refactored_code": refactored_code}
        return {"action": "unknown"}