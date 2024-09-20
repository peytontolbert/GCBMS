from typing import Dict
from src.database.node_manager import NodeManager
from src.agent.chat_with_ollama import ChatGPT
from src.agent.error_handler import ErrorHandler

class CodeModifier:
    def __init__(self):
        self.node_manager = NodeManager()
        self.llm_client = ChatGPT()
        self.error_handler = ErrorHandler()

    async def modify_code(self, node_id: str, new_content: str) -> Dict:
        """
        Updates the content of a specified code node.
        """
        try:
            # Update the node in the graph database
            updated_node = await self.node_manager.update_node(node_id, {"content": new_content})
            return updated_node
        except Exception as e:
            error_details = self.error_handler.handle_error(e)
            return {"error": error_details}

    async def generate_code(self, specification: Dict) -> str:
        """
        Generates code based on a given specification using LLM.
        """
        try:
            module = specification.get("module", "default")
            features = specification.get("features", [])
            feature_str = ", ".join(features)
            prompt = f"Generate a Python module named '{module}' with features: {feature_str}."
            code = await self.llm_client.generate(prompt)
            return code
        except Exception as e:
            error_details = self.error_handler.handle_error(e)
            return f"# Error generating code: {error_details}"