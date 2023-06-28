# Use the official Python base image with version 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Streamlit application will run
EXPOSE 8501

# Set the entrypoint command to run the Streamlit application
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
