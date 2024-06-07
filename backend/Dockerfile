# Use an official Python runtime as the base image
FROM python:3.13.0b1-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app/

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install application dependencies (if you have a requirements.txt file)
# Uncomment the following lines if needed:
 COPY requirements.txt /app/
 RUN pip install -r requirements.txt

EXPOSE 80
# Define the command to run your Python application
CMD ["python", "app.py"]

