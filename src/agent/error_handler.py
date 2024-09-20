from typing import Dict
import logging

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def handle_error(self, error: Exception) -> Dict:
        """
        Processes an exception and generates an appropriate response.
        """
        self.logger.error(f"Error: {str(error)}", exc_info=True)
        return {"error": str(error), "details": "An unexpected error occurred."}

    def generate_error_response(self, error: Exception) -> str:
        """
        Creates a user-friendly error message based on the exception.
        """
        return f"Sorry, something went wrong: {str(error)}"