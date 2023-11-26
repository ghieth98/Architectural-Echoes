FROM python:3.9

WORKDIR /app

# Copy the requirements file separately to leverage Docker layer caching
COPY requirements.txt .
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which Flask will run
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Activate the virtual environment and start the Flask app
CMD ["venv/bin/python", "-m", "flask", "run"]