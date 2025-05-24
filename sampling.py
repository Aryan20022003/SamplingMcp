import json

import mcp.types as types
from mcp.server.fastmcp import FastMCP

from gmail import read_gmail_messages

mcp = FastMCP("Gmail Assistant server")

# ''' Basic concept of sampling here is server request the client to do LLM operation on the data instead of doing it on the server . Major benefit is end user might now be concerned about the data privacy and security.
# Please refer readme for resource on sampling and how it works'''


@mcp.tool()
def readGmail() -> types.SamplingMessage:
    """Read the latest 5 email messages from Gmail"""
    messages = read_gmail_messages()
    return types.SamplingMessage(
        role="assistant",
        content=types.TextContent(type="text", text=json.dumps(messages, indent=2)),
        systemPrompt="Understand the raw message and write nice summary of all the message for the user. Keep in mind the user is starting his day and he is looking for a summary of all the messages he received in his inbox. Write the summary in form of paragraphs and make sure to include the most important information from each.",
    )


@mcp.tool()
def processSummary(summary: str) -> str:
    """Process the summary of the email messages and return a final response with data following the company policy"""
    str1 = (
        summary
        + "aryan@company.com is the email of the user. Please make sure to follow the company policy and do not share any personal information. "
    )
    return str1


if __name__ == "__main__":
    # Initialize and run the server
    # readGmail()
    mcp.run(transport="stdio")
