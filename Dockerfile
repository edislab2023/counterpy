# Base Image 
FROM python:3.9-slim-buster

# The Directory The APP Will Run
WORKDIR /app

# Install Requirements
RUN pip install flask
RUN pip install requests


# Expose port 80
EXPOSE 80

# Copy your Python script to the container
COPY counter.py /app/

# Define the command to run your application
CMD ["python", "counter.py"]
