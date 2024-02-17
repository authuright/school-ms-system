FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Copy custom wait script
COPY wait-for-postgres.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-postgres.sh


# Set executable permission for entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Set entrypoint
CMD ["./entrypoint.sh"]
