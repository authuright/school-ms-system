#!/bin/bash

set -e

host="$1"
shift
cmd="$@"
timeout=30 # Timeout in seconds
interval=5  # Interval between connection attempts

# Function to check if PostgreSQL is ready
wait_for_postgres() {
    start_time=$(date +%s)
    until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' >/dev/null 2>&1; do
        >&2 echo "Postgres is unavailable - sleeping"
        sleep "$interval"
        current_time=$(date +%s)
        elapsed_time=$((current_time - start_time))
        if [ "$elapsed_time" -ge "$timeout" ]; then
            >&2 echo "Timeout waiting for PostgreSQL to become available"
            exit 1
        fi
    done
}

wait_for_postgres

>&2 echo "Postgres is up - executing command"
exec "$cmd"
