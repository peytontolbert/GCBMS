from typing import Dict
class ErrorHandler:
    def handle_error(self, error: Exception) -> Dict:
        """
        Processes an exception and generates an appropriate response.
        """
        return {"error": str(error), "details": "An unexpected error occurred."}

    def generate_error_response(self, error: Exception) -> str:
        """
        Creates a user-friendly error message based on the exception.
        """
        return f"Sorry, something went wrong: {str(error)}"