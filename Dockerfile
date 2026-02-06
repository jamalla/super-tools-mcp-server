# Use a lightweight Python image
FROM python:3.12-slim-bookworm

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy dependency files first
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN uv pip install --system -r requirements.txt
RUN uv pip install --system .

# Copy source code
COPY src ./src
COPY README.md .

# Create the user
RUN useradd -m appuser
USER appuser

# Entry point (defaults to stdio mode)
# To run with SSE (if supported by library updates) or other flags, override CMD
ENTRYPOINT ["uv", "run", "super-tools"]
