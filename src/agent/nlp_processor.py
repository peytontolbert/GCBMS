import re
from typing import Dict

class NLPProcessor:
    def parse_input(self, user_message: str) -> Dict:
        """
        Parses the user's message to identify intent and extract entities.
        """
        # Simple intent and entity extraction logic (to be expanded)
        intent = "unknown"
        entities = {}

        if "generate" in user_message.lower():
            intent = "generate_code"
            match = re.search(r"generate a new (\w+)", user_message.lower())
            if match:
                entities["module"] = match.group(1)

        return {"intent": intent, "entities": entities}

    def generate_response(self, parsed_input: Dict) -> str:
        """
        Generates a response based on the parsed input.
        """
        intent = parsed_input.get("intent")
        if intent == "generate_code":
            module = parsed_input["entities"].get("module", "module")
            return f"Generating code for the new {module} module."
        return "I'm not sure how to help with that."