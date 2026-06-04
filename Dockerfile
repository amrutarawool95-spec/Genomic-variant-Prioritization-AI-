# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 10000 (Render's default port, though it dynamically assigns via $PORT)
EXPOSE 10000

# Run the application using Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]

