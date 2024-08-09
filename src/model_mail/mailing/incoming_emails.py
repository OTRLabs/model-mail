from __future__ import annotations



from typing import List, Optional


class IncomingEmailHandler:
    
    # use the __init__ to verify the connection to the postfix server. 
    async def __init__(self, email_config: dict[str, str]) -> None:
        pass