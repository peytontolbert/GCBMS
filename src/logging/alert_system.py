import smtplib
from typing import Dict

class AlertSystem:
    def __init__(self, smtp_server: str, smtp_port: int, admin_email: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.admin_email = admin_email
    
    def send_alert(self, alert_type: str, message: str) -> None:
        subject = f"Alert: {alert_type}"
        body = message
        email_message = f"Subject: {subject}\n\n{body}"
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.sendmail(self.admin_email, self.admin_email, email_message)
    
    def configure_alerts(self, settings: Dict) -> None:
        # Implement configuration logic
        pass