# Use the official lightweight Python image.
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image
WORKDIR /app
COPY . /app

# Install production dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the web service on container startup.
CMD ["functions-framework", "--target=hello_world"]
