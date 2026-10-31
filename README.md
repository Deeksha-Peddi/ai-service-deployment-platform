# AI Service Deployment Platform

A containerized Flask application deployed on AWS EC2 using Docker. This project demonstrates application containerization, Docker Hub image publishing, cloud deployment, health monitoring, and basic container security practices.

> **Note:** The inference endpoint is a simulated AI inference API. It demonstrates the structure of an AI service deployment rather than running an actual machine learning model.

## Project Overview

The application provides a simple web dashboard and REST API endpoints. It is packaged into a Docker container and deployed on an AWS EC2 Ubuntu server.

### Live Application

**Application:** http://18.212.246.31:8081

**Health Check:** http://18.212.246.31:8081/health

## Technology Stack

- **Backend:** Python, Flask
- **Application Server:** Gunicorn
- **Containerization:** Docker
- **Container Registry:** Docker Hub
- **Cloud Platform:** AWS EC2
- **Operating System:** Ubuntu 24.04
- **Instance Type:** AWS t3.micro
- **Container Security:** Non-root user execution

## Architecture

```text
          Developer
              |
              v
       Application Code
              |
              v
        Docker Build
              |
              v
        Docker Image
              |
              v
          Docker Hub
              |
              v
          AWS EC2
         (Ubuntu)
              |
              v
       Docker Container
          (Gunicorn)
              |
              v
       Port 8081:8081
              |
              v
       Public Web Access
```

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Web dashboard |
| `/health` | Application health check |
| `/api/info` | Application information |
| `/api/inference` | Simulated AI inference endpoint |

## Project Structure

```text
ai-service-deployment-platform/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── dashboard.js
```

## Run Locally Using Docker

### 1. Clone the repository

```bash
git clone https://github.com/Deeksha-Peddi/ai-service-deployment-platform.git
cd ai-service-deployment-platform
```

### 2. Build the Docker image

```bash
docker build -t ai-service-platform:v3 .
```

### 3. Run the container

```bash
docker run -d --name ai-service-container -p 8081:8081 ai-service-platform:v3
```

### 4. Verify the application

Open:

```text
http://localhost:8081
```

Check application health:

```text
http://localhost:8081/health
```

## Docker Hub

The Docker image is published on Docker Hub.

**Repository:** https://hub.docker.com/r/deeksha29/ai-service-platform

Pull the image:

```bash
docker pull deeksha29/ai-service-platform:v3
```

Run the published image:

```bash
docker run -d --name ai-service-container -p 8081:8081 deeksha29/ai-service-platform:v3
```

## AWS EC2 Deployment

The application is deployed on an AWS EC2 instance with the following configuration:

| Configuration | Details |
|---|---|
| Cloud Provider | AWS |
| Compute Service | EC2 |
| Operating System | Ubuntu 24.04 |
| Instance Type | t3.micro |
| Storage | 8 GiB gp3 |
| Container Runtime | Docker |
| Application Port | 8081 |
| Application Server | Gunicorn |

### Deployment Process

1. Provisioned an Ubuntu EC2 instance.
2. Configured access to the instance using AWS Systems Manager Session Manager.
3. Installed and configured Docker.
4. Pulled the application image from Docker Hub.
5. Started the container with port mapping.
6. Configured the container to restart automatically unless stopped.
7. Verified container health and application accessibility.

## Container Improvements

The Docker deployment includes the following improvements:

- **Gunicorn:** Runs the Flask application using a production-oriented WSGI server.
- **Multiple Workers:** Configured with two Gunicorn workers.
- **Non-root Execution:** Runs the application as a dedicated `appuser` instead of root.
- **Health Check:** Docker periodically checks the application's `/health` endpoint.
- **Restart Policy:** Uses `unless-stopped` to restart the container automatically after unexpected stops or server restarts.
- **Docker Ignore:** Excludes unnecessary files such as virtual environments, Git metadata, and environment files from the Docker build context.

## What I Learned

Through this project, I gained hands-on experience with:

- Building and managing Docker images and containers.
- Writing and improving Dockerfiles.
- Publishing container images to Docker Hub.
- Deploying containerized applications on AWS EC2.
- Configuring application ports and public access.
- Running Flask applications using Gunicorn.
- Implementing Docker health checks.
- Applying basic container security through non-root execution.
- Troubleshooting deployment and container-related issues.

## Author

**Deeksha Peddi**

GitHub: https://github.com/Deeksha-Peddi

---

*This project was developed as a hands-on DevOps deployment exercise.*