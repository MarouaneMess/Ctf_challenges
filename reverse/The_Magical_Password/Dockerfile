# Use a base image with necessary dependencies
FROM debian:latest

# Install necessary packages (netcat)
RUN apt-get update && apt-get install -y netcat

# Set working directory
WORKDIR /app

# Copy the challenge executable to the container
COPY challenge /app/challenge

# Give executable permission to the challenge
RUN chmod +x /app/challenge

# Expose port 4444 (to be used for nc)
EXPOSE 4444

# Use netcat to listen on port 4444 and execute the challenge
CMD ["nc", "-lk", "-p", "4444", "-e", "./challenge"]
