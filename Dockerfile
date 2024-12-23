# Use the Python 3.9 slim image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install  -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the working directory to where your server.py file is located
WORKDIR /app/flask-server

# Expose the port the application runs on (if applicable)
EXPOSE 5000

# Command to run the application
CMD ["python", "server.py"]
