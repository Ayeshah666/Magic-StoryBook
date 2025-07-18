# Use an official Python runtime as base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port
EXPOSE 8080

# Read the OpenRouter API key from environment (don't hardcode!)
# DO NOT hardcode your real key — remove this line:
# ENV OPENROUTER_API_KEY=sk-or-...

# Run the app
CMD ["python", "app.py"]
