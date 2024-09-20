from typing import List, Tuple, Dict
from datetime import datetime
class ThoughtLogStorage:
    def init(self):

        self.thought_logs = []
    def store_thought(self, thought_content: str, timestamp: datetime) -> None:
        self.thought_logs.append({
            'content': thought_content,
            'timestamp': timestamp
        })
    def get_thought_logs(self, user_id: str, time_range: Tuple[datetime, datetime]) -> List[Dict]:
        start, end = time_range
        return [
            log for log in self.thought_logs
            if start <= log['timestamp'] <= end
        ]
