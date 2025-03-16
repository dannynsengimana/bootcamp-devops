# DevOps Bootcamp Project

This project deploys a simple web application using Docker and Kubernetes.

## Project Directory

website-project/
├── backend
│      ├── app.py
│      └── requirements.txt
├── docker
│      ├── backend
│      │   └── dockerfile
│      └── frontend
│          └── dockerfile
├── frontend
│      └── index.html
├── kubernetes
│      ├── backend-configmap.yaml
│      ├── backend-deployment.yaml
│      ├── frontend-deployment.yaml
│      ├── redis-deployment.yaml
│      └── redis-secret.yaml
└── README.md

* **`frontend/`:** Contains the frontend code (HTML, JavaScript).
* **`backend/`:** Contains the backend application code (Python/Flask) and dependencies.
* **`docker/`:** Contains Dockerfiles for building the frontend and backend images.
    * `docker/frontend/dockerfile`: Dockerfile for the frontend.
    * `docker/backend/dockerfile`: Dockerfile for the backend.
* **`kubernetes/`:** Contains Kubernetes configuration files for deploying the application.
    * `kubernetes/backend-configmap.yaml`: ConfigMap for backend configuration.
    * `kubernetes/backend-deployment.yaml`: Deployment for the backend.
    * `kubernetes/frontend-deployment.yaml`: Deployment for the frontend.
    * `kubernetes/redis-deployment.yaml`: Deployment for Redis.
    * `kubernetes/redis-secret.yaml`: Secret for Redis password.
* **`README.md`:** This file, containing project information and deployment instructions.

* **Note:** The root directory is assumed to be `website-project/` for clarity in the rest of the document.

## Project Summary

This project showcases a basic web application with the following components:

* **Frontend:** A web interface (e.g., a "DevOps Bootcamp Content" page) built with HTML and JavaScript, allowing users to interact with a backend API.
* **Backend:** A Python Flask application that handles API requests (e.g., adding and retrieving modules) and interacts with the database.
* **Database:** Redis, an in-memory data store, used for data persistence.

The project is containerized using Docker and orchestrated using Kubernetes. It also utilizes ConfigMaps for configuration, Secrets for storing sensitive information, and Deployments with ReplicaSets for improved availability.

## Deployment Steps

For detailed deployment instructions, please refer to the documentation at `https://www.notion.so/irembo/Deploy-a-Project-Using-Kubernetes-Manifests-1b84e31d0fcf8048b211e104b8862813?pvs=4`.