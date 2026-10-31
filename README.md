# AI Service Deployment Platform

A Flask-based web application packaged with Docker and deployed on AWS EC2.

## Project Overview
This project demonstrates containerization and cloud deployment of a web application using Docker and AWS EC2.

## Technology Stack
- Python and Flask
- Docker
- AWS EC2 (Ubuntu 24.04)
- Docker Hub
- Git and GitHub

## Application Features
- Web dashboard
- Application health endpoint
- Application information endpoint
- Simulated AI inference API

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Dashboard |
| `/health` | GET | Health check |
| `/api/info` | GET | Application information |
| `/api/inference` | POST | Simulated inference |

## Docker Image
`deeksha29/ai-service-platform:v1`

## Deployment
The application is deployed on an AWS EC2 Ubuntu instance using Docker.

Public URL: http://18.212.246.31:8081

## Run Locally

```bash
docker build -t ai-service-platform:v1 .
docker run -d -p 8081:8081 ai-service-platform:v1
```

Open `http://localhost:8081` in your browser.

## Note
The inference endpoint returns simulated responses. It does not run an actual AI model.