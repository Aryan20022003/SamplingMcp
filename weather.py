import asyncio
import json
from typing import Any

import mcp.types as types
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from gmail import read_gmail_messages

mcp = FastMCP("Gmail Assistant server")
load_dotenv()


@mcp.tool()
def readGmail() -> types.SamplingMessage:
    """Read the latest 5 email messages from Gmail"""
    messages = read_gmail_messages()
    return types.SamplingMessage(
        role="assistant",
        content=types.TextContent(type="text", text=json.dumps(messages, indent=2)),
        systemPrompt="Understand the raw message and write nice summary of all the message for the user. Keep in mind the user is starting his day and he is looking for a summary of all the messages he received in his inbox. ",
    )


if __name__ == "__main__":
    # Initialize and run the server
    readGmail()
    mcp.run(transport="stdio")
