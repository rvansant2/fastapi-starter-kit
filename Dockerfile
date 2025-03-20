FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Optionally, define a build argument for API port
ARG API_PORT=8000
ENV PORT=${API_PORT}

# Set PYTHONPATH so that the "app" package is discoverable
ENV PYTHONPATH=/app

# Upgrad pip
RUN pip install --upgrade pip

# Copy and install requirements
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Copy src files to app
COPY ./src/app /app/app

# Expose port specified
EXPOSE ${API_PORT}

# Execute app
CMD uvicorn app.main:app --reload --host 0.0.0.0 --port ${API_PORT} --workers 4