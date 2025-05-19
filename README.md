docker build -t blog .
docker image list
docker run -p 8000:8000 blog


<!-- this will listen for changes -->
docker run -v $(pwd):/app -p 8000:8000 blog
    - NOTE: - -v $(pwd):/app → mounts your current host directory (project code) into the container at /app.

docker compose up --build
    - This will build and run with docker compose


docker compose exec <service_name> python manage.py migrate 
    - NOTE: To run django specific commands (NOTE: The django web container must be running.)
    - in our own case, the command will be:
    - docker compose exec blog python manage.py migrate
    - docker compose exec blog python manage.py createsuperuser


docker ps
    - Lists all currently running Docker containers.
    - Shows container ID, image, command, status, port mappings, and container name.

docker exec -it <container_name_or_id> bash
    - Starts an interactive shell (bash) inside a running container.
    - Replace <container_name_or_id> with either the container name (blog-db-1) or ID (dc6ea9bd8502)
    Command in Action:
        - docker exec -it dc6ea9bd8502 bash
        NOTE: This will open an interactive bash shell for the container with the provided ID.

docker stop <container_name_or_id>
    - This stops a running container

docker start <container_name_or_id>
    - This starts a container