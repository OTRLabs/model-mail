from __future__ import annotations
from typing import List, Optional
from email.message import EmailMessage
import asyncio
from rich.console import Console
import aiosmtplib
from ..config.configurations import Settings, MailingConfigs

class IncomingEmailHandler:
    
    async def __init__(self, console: Console, email_config: MailingConfigs) -> None:
        self.console: Console = console
        self.email_config: MailingConfigs = email_config
        self.smtp_client = aiosmtplib.SMTP(hostname=self.email_config.smtp_server, port=self.email_config.smtp_port)
        
        try:
            await self.smtp_client.connect()
            self.console.print("Connected to the SMTP server")
        except Exception as e:
            self.console.print(f"Failed to connect to the SMTP server: {e}", style="bold red")
            raise
        
        try:
            await self.smtp_client.login(self.email_config.smtp_user, self.email_config.smtp_password)
            self.console.print("Logged in to the SMTP server")
        except Exception as e:
            self.console.print(f"Failed to login to the SMTP server: {e}", style="bold red")
            raise
