FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only source code (exclude tests, venv, etc. via .dockerignore)
COPY api/ ./api/
COPY core/ ./core/
COPY data/ ./data/
COPY infra/ ./infra/
COPY README.md .

# Switch to non-root user
USER 1000

# Expose Cloud Run default port
EXPOSE 8080

# Run FastAPI app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]