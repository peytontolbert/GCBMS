# Agent Module

## Overview
The Agent module is a core component of our LLM-powered system, designed to process user inputs, execute actions, and manage code modifications. It leverages the Ollama API for natural language processing and code generation.

## Components

1. **NLPProcessor**: Parses user inputs to identify intents and entities.
2. **ActionEngine**: Determines and executes actions based on parsed inputs.
3. **CodeModifier**: Handles code generation and modifications.
4. **ErrorHandler**: Manages exceptions and generates user-friendly error messages.
5. **ThoughtLogger**: Logs internal reasoning and decision-making processes.
6. **ChatGPT**: Interfaces with the Ollama API for LLM functionalities.

## Usage

```python
from src.agent import LLMAgent

agent = LLMAgent()
response = await agent.handle_user_message("Generate a new authentication module")
print(response)
```

## Key Features

- Natural language understanding and processing
- Dynamic code generation and modification
- Robust error handling and logging
- Integration with Ollama API for advanced language model capabilities

## Configuration

Ensure the Ollama API is properly configured and accessible. Update the `base_url` in `ChatGPT` class if necessary.

## Dependencies

- aiohttp
- jsonschema
- tenacity

## Testing

Run unit tests to ensure all components are functioning correctly:

```bash
python -m unittest discover tests/agent
```

## Contributing

Please refer to the main project's contributing guidelines when making changes to this module.
