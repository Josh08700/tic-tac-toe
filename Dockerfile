FROM python:3.13-slim

WORKDIR /app

# Copy uv binary from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 1. Copy dependency definition files
COPY pyproject.toml uv.lock* README.md ./

# 2. Install external dependencies (skips looking for a local package)
RUN uv sync --frozen --no-cache --no-install-project

# 3. Copy application code
COPY src ./src

ENV NICEGUI_HOST=0.0.0.0

# 4. Run application
CMD ["uv", "run", "python", "-m", "src.gui"]









