# Use official Python 3.10 image as the base
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code
COPY . .

# Expose port 5000 (where Flask runs)
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]