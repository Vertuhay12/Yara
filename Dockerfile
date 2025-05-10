FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y ffmpeg && pip install -r requirements.txt

COPY bot.py .

CMD ["python", "bot.py"]
