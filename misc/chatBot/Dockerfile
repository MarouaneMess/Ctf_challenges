
FROM python:3.11-slim
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
RUN pip install nltk

RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"

COPY chatBot.py /app/chatBot.py
COPY flag.txt /app/flag.txt

WORKDIR /app

EXPOSE 5000

CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:python chatBot.py"]