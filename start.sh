#!/bin/bash

# Build the Docker image
docker build -t joules_of_siam_webapp ./docker

# Stop and remove any existing container with the same name
docker rm -f joules_of_siam_webapp 2>/dev/null || true

# Run the Docker container in detached mode with a volume mount
docker run -d --name joules_of_siam_webapp \
  -v $(pwd):/app \
  -p 8000:8000 \
  joules_of_siam_webapp
