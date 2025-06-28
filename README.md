This a code for basic MCP Server and Client in action.

Libraries used for building MCP server:
1. fastmcp
2. pygit2 - to access the contents of the git repository. (Documentation - https://www.pygit2.org/)

Libraries used for building MCP client:
1. mcp-use - is the open source way to connect any LLM to any MCP server and build custom MCP agents that have tool access, without using closed source or application clients. (Documentation - https://github.com/mcp-use/mcp-use)
2. langchain_groq - Used to access the open source models.

server.py contains the code logic for the server.

client.py contains the code logic for the client.

mcp.json contains the information about the servers available to use(only one in our case but there can be multiple). Here the server is running in local but you can host you server and add your logic/command to access the server remotely.