# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the container
COPY . .

# Specify the command to run your Flask app within the container
CMD ["python", "bob-the-butler.py"]
