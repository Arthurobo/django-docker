# Docker Commands for Blog Application

This README contains essential Docker commands for managing the blog application container and its services.

## Basic Container Operations

### Building and Running
```bash
# Build the Docker image
docker build -t blog .

# List all Docker images
docker image list

# Run the container with port mapping
docker run -p 8000:8000 blog
```

### Development Mode with Volume Mounting
```bash
# Run container with volume mounting for development
docker run -v $(pwd):/app -p 8000:8000 blog
```
> **Note**: The `-v $(pwd):/app` flag mounts your current host directory (project code) into the container at `/app`, enabling live code changes without rebuilding.

## Docker Compose Operations

### Starting Services
```bash
# Build and start all services defined in docker-compose.yml
docker compose up --build
```

### Django Management Commands
```bash
# Run Django migrations
docker compose exec blog python manage.py migrate

# Create a superuser
docker compose exec blog python manage.py createsuperuser
```
> **Note**: These commands require the Django web container to be running.

## Container Management

### Viewing Containers
```bash
# List all running containers
docker ps
```
This command displays:
- Container ID
- Image name
- Command
- Status
- Port mappings
- Container name

### Container Shell Access
```bash
# Access container shell
docker exec -it <container_name_or_id> bash
```
> **Example**: `docker exec -it dc6ea9bd8502 bash`
> 
> This opens an interactive bash shell inside the specified container.

### Container Lifecycle
```bash
# Stop a running container
docker stop <container_name_or_id>

# Start a stopped container
docker start <container_name_or_id>
```

## Best Practices
1. Always use `docker compose up --build` during development to ensure all services are properly configured
2. Use volume mounting (`-v`) during development for live code changes
3. Remember to run migrations after any database schema changes
4. Use `docker ps` to verify container status before running management commands

## To Remove all containers (both running and stopped) use the command below
`docker rm $(docker ps -aq)`
