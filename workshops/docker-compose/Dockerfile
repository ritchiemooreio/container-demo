# web/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install Flask
RUN pip install flask redis

# Copy the application code
COPY web/app.py .

# Expose the Flask port
EXPOSE 8080

# Run the Flask application
CMD ["python", "app.py"]
