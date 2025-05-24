# Idea of Sampling and data privacy

This repository demonstrates how to use the "Sampling" feature of the Model Context Protocol (MCP) to summarize Gmail emails programmatically. The server is built using the `FastMCP` library and integrates with the Gmail API to fetch and summarize the latest emails.

- Sampling is technique where tools will provide data and instruction to model and your private model will provide the output. This is a great way to keep your data private and not share it with the model. The sampling feature of MCP allows you to do this in a very easy way.

## Prerequisites

1. **Google API Credentials**:
   - You need a `credentials.json` file from Google to authenticate with the Gmail API.
   - Follow the instructions at [Gmail API Quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python) to set up your Google Cloud project and download the `credentials.json` file.

2. **Python Environment**:
   - Ensure you have Python installed along with the required dependencies. This project uses `poetry` for dependency management.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd weather
   ```

2. Install dependencies using `poetry`:
   ```bash
   poetry install
   ```

3. Place your `credentials.json` file in the root directory of the project.

## Running the Server

1. Authenticate with Gmail:
   - The first time you run the server, it will prompt you to authenticate with your Google account. This will generate a `token.json` file for subsequent runs.

2. Start the MCP server:
   ```bash
   poetry run python weather.py
   ```

## How It Works

- The server uses the Gmail API to fetch the latest 5 emails from your inbox.
- The `readGmail` tool processes these emails and generates a summary using the MCP Sampling feature.
- The summary is tailored to help users start their day with a concise overview of their inbox.

## Key Files

- `weather.py`: Contains the MCP server implementation and the `readGmail` tool.
- `gmail.py`: Handles Gmail API authentication and email fetching.

## References

- [Gmail API Quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python): Learn how to programmatically access Gmail.
- [MCP Sampling Documentation](https://modelcontextprotocol.io/docs/concepts/sampling): Understand the Sampling feature of MCP.