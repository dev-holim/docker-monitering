FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    && apt-get clean


WORKDIR /webapp

COPY . .

ENV TZ=Asia/Seoul

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 8000
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
#CMD ["gunicorn", "-k", "eventlet", "-w", "1", "run:app"]