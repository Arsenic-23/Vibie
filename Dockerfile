# Use an official lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python3", "main.py"]