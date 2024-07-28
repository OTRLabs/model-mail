from __future__ import annotations
from rich.console import Console

from dotenv import load_dotenv
import os

load_dotenv()


class BasicConfigs:
    def __init__(self) -> None:
        self.app_name: str = os.getenv("SYSTEM_APP_NAME")
        self.app_version: str = os.getenv("SYSTEM_APP_VERSION")
        self.app_author: str = os.getenv("SYSTEM_APP_AUTHOR")
        self.app_description: str = os.getenv("SYSTEM_APP_DESCRIPTION")
        


class MailingConfigs:
    def __init__(self, console: Console) -> None:
        self.console: Console = console
        self.smtp_server: str = os.getenv("SYSTEM_SMTP_SERVER")
        self.smtp_port: int = int(os.getenv("SYSTEM_SMTP_PORT"))
        self.smtp_user: str = os.getenv("SYSTEM_SMTP_USER")
        self.smtp_password: str = os.getenv("SYSTEM_SMTP_PASSWORD")
        self.sender_email: str = os.getenv("SYSTEM_SENDER_EMAIL")
        self.receiver_email: str = os.getenv("SYSTEM_RECEIVER_EMAIL")




class Settings:
    mail_config: MailingConfigs = MailingConfigs(Console())