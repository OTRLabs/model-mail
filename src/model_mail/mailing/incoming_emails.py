from __future__ import annotations



from typing import List, Optional

from rich.console import Console

from ..config.configurations import Settings, MailingConfigs

class IncomingEmailHandler:
    
    # use the __init__ to verify the connection to the postfix server. 
    async def __init__(self, console: Console, email_config: MailingConfigs) -> None:
        pass