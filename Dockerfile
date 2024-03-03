# Specify the Python version and base image
ARG PYTHON_VERSION=3.9.6
FROM python:${PYTHON_VERSION}-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=1 \
    PATH="/root/.local/bin:$PATH" 

# Ensure pipenv executable is in the PATH

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    libsm6 libxext6 libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# install something idk
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install project dependencies within the Pipenv virtual environment
RUN pipenv install --deploy --ignore-pipfile

# Copy the source code into the container
COPY . .

# Expose the port that the application listens on
EXPOSE 8001

# Command to run the application within the Pipenv virtual environment
CMD ["pipenv", "run", "python", "main.py"]
