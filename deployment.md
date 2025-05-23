# Deploying a Django Application with Docker to Production

## Prerequisites
- Ubuntu server
- Access to official Docker documentation: [Docker Installation Guide](https://docs.docker.com/engine/install/ubuntu/)

## Installation Steps

### 1. Install Docker using the apt repository

First, set up the Docker apt repository to install and update Docker:

```bash
# Add Docker's official GPG key
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### 2. Install Docker Packages

Install the latest version of Docker:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 3. Verify Installation

Verify that Docker is installed correctly:

```bash
sudo docker run hello-world
docker --version
docker compose version
```

### 4. Configure User Permissions

Allow the ubuntu user to run Docker commands without sudo:

```bash
sudo usermod -aG docker ubuntu
newgrp docker
sudo usermod -aG docker $USER
```

## Deploying Your Application

### 1. Set Up Project Directory

Create and navigate to the project directory:

```bash
mkdir -p /home/ubuntu/src
cd /home/ubuntu/src
```

### 2. Clone Your Repository

Initialize git and pull your code:

```bash
git init
git pull https://github.com/Arthurobo/django-docker.git
```

### 3. Build and Run

Next we have to add our production .env file and all necessary credentials

### 4. Build and Run

Start your application using Docker Compose:

```bash
docker compose up -d --build
```

Now our application is running successfully, nice.

Next is to know how to get logs, all logs for all images:

1. Get logs from any of our image container service with the command:

```bash
docker logs <container_name_or_id>
```

To see logs in real time, use this command:

```bash
docker logs -f <container_name_or_id>
```

To see real time logs for multiple services:

```bash
docker-compose logs -f <container_name_or_id> <container_name_or_id> <container_name_or_id>
```

e.g:

```bash
docker-compose logs -f blog celery celery-beat nginx
```

To add timestamps to logs, use the --timestamps flag:

```bash
docker logs -f --timestamps <container_name>
```

**Note**: Always use `docker ps` to get container's name and IDs
