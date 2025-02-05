FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    socat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY securebank /app/securebank
COPY flag.txt /app/flag.txt

RUN chmod +x /app/securebank

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/app/securebank"]