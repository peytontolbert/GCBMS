import logging

class ThoughtLogger:
    def __init__(self):
        self.logger = logging.getLogger("ThoughtLogger")
        handler = logging.FileHandler("thought_logs.log")
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_thought(self, thought_content: str) -> None:
        """
        Logs a piece of internal reasoning or decision-making content.
        """
        self.logger.info(thought_content)