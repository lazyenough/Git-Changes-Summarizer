import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq

load_dotenv()

async def gitSummarizer():
    mcp_client = MCPClient.from_config_file("mcp.json")

    llm = ChatGroq(
        groq_api_key = os.getenv("GROQ_API_KEY"),
        model_name = "llama3-70b-8192"
    )

    agent = MCPAgent(llm = llm, client = mcp_client)

    repo_path = "LOCAL REPO PATH TO BE ANALYZED"
    answer = await agent.run(f"Summarize the changes in the following repository. Repo Link - {repo_path}")

    print(answer)


async def main():
    await gitSummarizer()

if __name__ == "__main__":
    asyncio.run(main())