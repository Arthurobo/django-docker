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
