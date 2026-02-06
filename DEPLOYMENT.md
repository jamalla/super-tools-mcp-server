# Deployment Guide for Super Tools MCP Server

This server conforms to the Model Context Protocol (MCP). It allows you to run it locally or deploy it to the cloud.

## 🐳 Option 1: Docker (Recommended for Cloud)

I have included a `Dockerfile` to containerize the application.

### Build the Image
```bash
docker build -t super-tools .
```

### Run Locally (Stdio)
This is useful for connecting to the Inspector running in Docker.
```bash
docker run -i super-tools
```

### Deploy to Render / Railway / Fly.io

Because this MCP server runs over **Stdio** by default, it does not use an HTTP port. This works best for:
1.  **Background Workers**: Deploy as a worker (not a web service) if it's meant to process tasks from a queue (though MCP isn't usually used this way).
2.  **MCP Registries**: Platforms like Smithery or Glama can ingest the Docker image.

**Important**: If you need to deploy this as a **Web Service** (e.g., exposing an SSE endpoint), you typically need to wrap it with an ASGI server. If `super-tools` supports SSE flags in the future, you would modify the Dockerfile command:

```dockerfile
# Example if SSE is supported
CMD ["uv", "run", "super-tools", "--transport", "sse", "--port", "8000"]
```

## 💻 Option 2: Local Usage (Free & Easiest)

You don't need to "deploy" it to use it with Claude Desktop. Just run it locally!

**Claude Desktop Config:**
```json
{
  "mcpServers": {
    "super-tools": {
      "command": "uv",
      "args": ["run", "super-tools"]
    }
  }
}
```

## ☁️ Option 3: Python Hosting (Glitch / pythonanywhere)

You can clone this repository to services like Glitch or pythonanywhere.
 Ensure you install dependencies:
```bash
pip install -r requirements.txt
pip install .
```
Then run the entry point `super-tools`.
