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

# Set environment variable for OpenAI key (if using Docker secrets or envs)
# You can also override this from the CLI or Railway
ENV OPENAI_API_KEY=your-openrouter-key-here

# Run the app
CMD ["python", "app.py"]
