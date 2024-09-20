# LLM Agent Module Implementation

## Overview
The `LLMAgent` module serves as the core component of the LLM-powered system, responsible for processing user inputs, determining appropriate actions, modifying codebases, handling errors, and logging internal processes. It integrates various sub-components to ensure seamless interaction and robust functionality.

## Components

### 1. NLPProcessor
**Description:**
Handles the parsing of user messages to identify intents and extract relevant entities using the `ChatGPT` client.

**Class: `NLPProcessor`**

**Methods:**
- `parse_input(user_message: str) -> Dict`
  - **Description:** Utilizes the LLM to analyze the user's message and extract intent and entities.
  - **Parameters:**
    - `user_message`: The raw input message from the user.
  - **Returns:** A dictionary containing the parsed `intent` and `entities`.

- `generate_response(parsed_input: Dict) -> str`
  - **Description:** Generates a textual response based on the parsed input.
  - **Parameters:**
    - `parsed_input`: The dictionary output from `parse_input`.
  - **Returns:** A string response tailored to the identified intent.

**Dependencies:**
- `ChatGPT` from `chat_with_ollama.py`

**Example Usage:**
python
```
nlp_processor = NLPProcessor()
parsed = nlp_processor.parse_input("Generate a new authentication module.")
response = nlp_processor.generate_response(parsed)
```

---
### 2. ActionEngine
**Description:**
Determines and orchestrates actions based on the parsed user inputs. It interacts with the `CodeModifier` and `ChatGPT` to execute actions like code generation and refactoring.

**Class: `ActionEngine`**

**Methods:**
- `decide_action(parsed_input: Dict) -> str`
  - **Description:** Determines the appropriate action based on the user's intent.
  - **Parameters:**
    - `parsed_input`: The output from `NLPProcessor.parse_input`.
  - **Returns:** A string identifier for the action (e.g., `"generate_code"`).

- `extract_parameters(parsed_input: Dict) -> Dict`
  - **Description:** Extracts necessary parameters required to execute the determined action.
  - **Parameters:**
    - `parsed_input`: The output from `NLPProcessor.parse_input`.
  - **Returns:** A dictionary of parameters relevant to the action.

- `execute_action(action: str, parameters: Dict) -> Dict`
  - **Description:** Executes the specified action using the provided parameters.
  - **Parameters:**
    - `action`: The action identifier.
    - `parameters`: A dictionary of parameters for the action.
  - **Returns:** A dictionary containing the result of the action.

**Dependencies:**
- `CodeModifier` from `code_modifier.py`
- `ErrorHandler` from `error_handler.py`
- `ChatGPT` from `chat_with_ollama.py`

**Example Usage:**
python
```
action_engine = ActionEngine()
action = action_engine.decide_action(parsed_input)
result = action_engine.execute_action(action, parameters)
```

---

### 3. CodeModifier
**Description:**
Manages modifications to the codebase, including updating existing code nodes and generating new code based on specifications.

**Class: `CodeModifier`**

**Methods:**
- `modify_code(node_id: str, new_content: str) -> Dict`
  - **Description:** Updates the content of a specified code node in the graph database.
  - **Parameters:**
    - `node_id`: The identifier of the node to modify.
    - `new_content`: The new code content to replace the existing one.
  - **Returns:** A dictionary representing the updated node.

- `generate_code(specification: Dict) -> str`
  - **Description:** Generates code based on provided specifications.
  - **Parameters:**
    - `specification`: A dictionary detailing the code requirements.
  - **Returns:** A string containing the generated code.

**Dependencies:**
- `NodeManager` from `node_manager.py`

**Example Usage:**
python
```
code_modifier = CodeModifier()
updated_node = code_modifier.modify_code(node_id="node123", new_content="def new_function(): pass")
generated_code = code_modifier.generate_code(specification={"module": "auth", "features": ["login", "signup"]})
```

---

### 4. ErrorHandler
**Description:**
Handles exceptions and errors, ensuring that the system responds gracefully and logs necessary details for troubleshooting.

**Class: `ErrorHandler`**

**Methods:**
- `handle_error(error: Exception) -> Dict`
  - **Description:** Processes an exception and generates a structured response containing error details.
  - **Parameters:**
    - `error`: The exception instance to handle.
  - **Returns:** A dictionary with error information.

- `generate_error_response(error: Exception) -> str`
  - **Description:** Creates a user-friendly error message based on the exception.
  - **Parameters:**
    - `error`: The exception instance to encapsulate in the response.
  - **Returns:** A string containing the error message for the user.

**Dependencies:**
- `logging`

**Example Usage:**
python
```
error_handler = ErrorHandler()
try:
result = risky_operation()
except Exception as e:
error_details = error_handler.handle_error(e)
error_message = error_handler.generate_error_response(e)
```

---

### 5. ThoughtLogger
**Description:**
Logs the internal reasoning and decision-making processes of the `LLMAgent` for auditing and analysis purposes.

**Class: `ThoughtLogger`**

**Methods:**
- `log_thought(thought_content: str) -> None`
  - **Description:** Logs a piece of internal reasoning or decision-making content.
  - **Parameters:**
    - `thought_content`: The content to log.
  - **Returns:** None

**Dependencies:**
- `logging`

**Example Usage:**
python
```
thought_logger = ThoughtLogger()
thought_logger.log_thought("Decided to create a new authentication module based on user request.")
```

---

### 6. ChatGPT
**Description:**
Interfaces with the Ollama API to leverage LLM functionalities for processing and generating natural language content.

**Class: `ChatGPT`**

**Methods:**
- `generate(prompt: str) -> str`
  - **Description:** Sends a prompt to the Ollama API and retrieves the generated response.
  - **Parameters:**
    - `prompt`: The input text to send to the LLM.
  - **Returns:** A string containing the generated text.

- `robust_chat_with_ollama(system_prompt: str, user_prompt: str) -> Dict[str, Any]`
  - **Description:** Engages in a robust conversation with Ollama, ensuring valid JSON responses.
  - **Parameters:**
    - `system_prompt`: The system-level prompt.
    - `user_prompt`: The user's input prompt.
  - **Returns:** A dictionary containing the LLM's response.

- Additional helper methods for handling JSON extraction and retries.

**Dependencies:**
- `aiohttp`, `asyncio`, `json`, `re`, `tenacity`, `jsonschema`, `requests`, `time`, `logging`

**Example Usage:**
python
```
ollama_client = ChatGPT()
response = await ollama_client.generate("Generate a Python function for user authentication.")
```

---

### 7. LLMAgent
**Description:**
Coordinates all components to handle user messages, perform actions, modify codebases, handle errors, and generate responses.

**Class: `LLMAgent`**

**Methods:**
- `handle_user_message(user_message: str) -> str`
  - **Description:** Processes a user's message by parsing input, deciding actions, executing them, and generating a response.
  - **Parameters:**
    - `user_message`: The raw input message from the user.
  - **Returns:** A string response to be sent back to the user.

- `generate_response(result: Dict[str, Any]) -> str`
  - **Description:** Formats the action results into a user-friendly response.
  - **Parameters:**
    - `result`: The dictionary containing action results.
  - **Returns:** A string containing the final response.

**Dependencies:**
- `NLPProcessor`, `ActionEngine`, `ErrorHandler`, `ThoughtLogger`, `ChatGPT`, `logging`

**Example Usage:**

python
```
from src.agent import LLMAgent
agent = LLMAgent()
response = await agent.handle_user_message("Generate a new authentication module")
print(response)
```

---

## Workflow

1. **Receiving User Message:**
   - The `LLMAgent` receives a user message through the `handle_user_message` method.

2. **Parsing Input:**
   - `NLPProcessor` parses the message to identify intent and extract entities.

3. **Logging Thought:**
   - `ThoughtLogger` logs the parsed input for auditing.

4. **Deciding Action:**
   - `ActionEngine` determines the appropriate action based on the parsed intent.

5. **Extracting Parameters:**
   - `ActionEngine` extracts necessary parameters for the action.

6. **Executing Action:**
   - Depending on the action (e.g., `generate_code`, `refactor_code`), `ActionEngine` interacts with `CodeModifier` and `ChatGPT` to perform the required operations.

7. **Logging Thought:**
   - All decisions and results are logged by `ThoughtLogger`.

8. **Generating Response:**
   - `LLMAgent` formats the results into a user-friendly response.

9. **Error Handling:**
   - Any exceptions encountered are managed by `ErrorHandler`, and appropriate messages are logged and returned to the user.

---

## Error Handling Strategy

- **Exception Catching:**
  - All critical operations within `LLMAgent` are wrapped in try-except blocks to catch and handle exceptions gracefully.

- **Logging:**
  - Detailed error information is logged using `ErrorHandler` and `ThoughtLogger` for later analysis.

- **User Feedback:**
  - Users receive clear and concise error messages without exposing sensitive internal details.

---

## Logging Mechanism

- **Thought Logging:**
  - Internal decisions and reasoning are logged to `thought_logs.log` via the `ThoughtLogger` for transparency and debugging.

- **Error Logging:**
  - Errors and exceptions are logged with traceback information to facilitate troubleshooting.

---

## Dependencies and Integration

- **External Services:**
  - **Ollama API:** Utilized by `ChatGPT` for LLM functionalities.
  
- **Internal Modules:**
  - `NodeManager` from `node_manager.py` is used by `CodeModifier` to interact with the graph database.

- **Asynchronous Operations:**
  - The system leverages asynchronous programming (`asyncio`, `aiohttp`) to handle I/O-bound tasks efficiently.

---

## Configuration

- **Environment Variables:**
  - The `ChatGPT` class uses the `base_url` for the Ollama API, which can be configured as needed.

- **Logging Configuration:**
  - Logging levels and handlers are set up within each class to ensure appropriate logging behavior.

---

## Testing

- **Unit Tests:**
  - Each component (`NLPProcessor`, `ActionEngine`, `CodeModifier`, etc.) should have corresponding unit tests to validate their functionality.

- **Integration Tests:**
  - Tests should verify the interactions between components, ensuring that the workflow from receiving a user message to generating a response operates correctly.

- **Continuous Integration:**
  - CI pipelines (e.g., GitHub Actions) are set up to run tests automatically on code commits to maintain code quality.

---

## Deployment Considerations

- **Containerization:**
  - The module can be containerized using Docker for consistent deployment environments.

- **Orchestration:**
  - Deployment can be managed using Kubernetes, facilitating scalability and high availability.

- **Rollback Procedures:**
  - Maintain previous deployment versions to enable quick rollbacks in case of failures.

---

## Conclusion

The `LLMAgent` module is meticulously designed to handle complex interactions involving natural language processing, action orchestration, code modification, and robust error handling. Its modular architecture ensures maintainability and scalability, while comprehensive logging and testing strategies uphold system reliability and performance.
