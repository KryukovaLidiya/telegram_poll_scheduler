FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir requests apscheduler

ENTRYPOINT ["python", "send_poll.py"]
CMD []
