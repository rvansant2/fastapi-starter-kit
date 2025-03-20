##############################
# Base stage
##############################
FROM python:3.12-slim as base
WORKDIR /app
ENV PYTHONPATH=/app

##############################
# Builder stage: Install dependencies
##############################
FROM base as builder

# Install any build dependencies (e.g. gcc) if needed
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements file and install dependencies into a local directory
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

##############################
# Runtime stage: Minimal image for running the app
##############################
FROM base as runtime

# Copy installed Python packages from the builder stage.
# The --user installation typically puts packages into /root/.local.
COPY --from=builder /root/.local /root/.local

# Update PATH so that executables from /root/.local/bin are available
ENV PATH="/root/.local/bin:${PATH}"

# Copy the application code.
# Assuming your project structure is:
# src/
#   app/
#     main.py
#     core/...
#     home/...
COPY src/app /app/app

# Optionally, pass build-time variable for API_PORT.
ARG API_PORT=8000
ENV API_PORT=${API_PORT}

# Expose the API port.
EXPOSE ${API_PORT}

# Execute app
CMD uvicorn app.main:app --reload --host 0.0.0.0 --port ${API_PORT} --workers 4