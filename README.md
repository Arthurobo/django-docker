docker build -t blog .
docker image list
docker run -p 8000:8000 blog


<!-- this will listen for changes -->
docker run -v $(pwd):/app -p 8000:8000 blog
    - NOTE: - -v $(pwd):/app → mounts your current host directory (project code) into the container at /app.