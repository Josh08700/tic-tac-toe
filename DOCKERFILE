FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy uv binary from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 1. Copy dependency files first (for Docker layer caching)
COPY pyproject.toml uv.lock* README.md ./

# 2. Install dependencies ONLY (skips installing your actual project)
RUN uv sync --frozen --no-cache --no-install-project

# 3. Copy application source code
COPY src ./src

# 4. Install your project package now that src/ exists
RUN uv sync --frozen --no-cache

# Run NiceGUI app explicitly targeting src/gui.py
ENV NICEGUI_HOST=0.0.0.0
CMD ["uv", "run", "python", "-m", "src.gui"]













