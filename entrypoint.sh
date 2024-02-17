#!/bin/bash

# Wait for PostgreSQL to initialize
wait-for-postgres.sh $POSTGRES_HOST:5432

# Start Flask application
python server.py