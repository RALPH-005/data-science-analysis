FROM python:3.9-slim

# Install only the bare essentials
RUN apt-get update && apt-get install -y wget procps && apt-get clean

# Copy your scripts
COPY . .

# Start the entrypoint script
CMD ["python", "entrypoint.py"]
