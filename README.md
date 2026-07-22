<div align="center">

# Enterprise AI KnowledgeOps Platform

An AI-powered Enterprise Knowledge Management Platform that enables organizations to securely upload documents and receive intelligent, context-aware answers using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5)
![Amazon EKS](https://img.shields.io/badge/AWS-EKS-FF9900)
![Amazon ECR](https://img.shields.io/badge/AWS-ECR-FF9900)
![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20)
![Redis](https://img.shields.io/badge/Redis-Cache-DC382D)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# Overview

Enterprise AI KnowledgeOps Platform is a full-stack AI-powered document intelligence system that enables organizations to securely manage documents and retrieve accurate answers using Retrieval-Augmented Generation (RAG).

Users can upload PDF documents, which are processed asynchronously using Apache Kafka, converted into vector embeddings with FAISS, and queried using Groq LLM for intelligent, context-aware responses. The application is containerized with Docker and deployed on Amazon EKS using Kubernetes.

---

# Key Features

- Secure JWT Authentication
- PDF Document Upload
- Retrieval-Augmented Generation (RAG)
- Semantic Search using FAISS
- AI-powered Question Answering with Groq LLM
- Apache Kafka Event-Driven Processing
- Redis Response Caching
- PostgreSQL Database
- Dockerized Multi-Container Architecture
- Kubernetes Deployment on Amazon EKS
- Amazon ECR for Container Registry
- AWS Application Load Balancer (ALB) Ingress
- Infrastructure Monitoring with Prometheus & Grafana
- RESTful APIs using FastAPI

---

# System Architecture

```text
                        +----------------------+
                        |      React UI        |
                        +----------+-----------+
                                   |
                             REST API
                                   |
                        +----------v-----------+
                        |      FastAPI         |
                        +----------+-----------+
                                   |
        ---------------------------------------------------------
        |                 |                |                    |
        ▼                 ▼                ▼                    ▼
 PostgreSQL         Redis Cache      Apache Kafka        JWT Authentication
                                            |
                                            ▼
                                    Kafka Consumer
                                            |
                                            ▼
                                     PDF Processing
                                            |
                                            ▼
                                     FAISS Vector Store
                                            |
                                            ▼
                                         Groq LLM
                                            |
                                            ▼
                                     AI Generated Response
```

---

# Deployment Architecture

```text
                     GitHub Repository
                             │
                             ▼
                      Docker Build
                             │
                             ▼
                       Amazon ECR
                             │
                             ▼
                   Amazon EKS Cluster
                             │
        ------------------------------------------------
        │               │             │               │
        ▼               ▼             ▼               ▼
   Frontend Pod   Backend Pod   PostgreSQL Pod   Redis Pod
                                        │
                                        ▼
                                   Kafka Pod
                                        │
                                        ▼
                           AWS ALB Ingress Controller
                                        │
                                        ▼
                                    End Users
```

---

# Technology Stack

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios

## Backend

- FastAPI
- Python
- SQLAlchemy
- JWT Authentication

## Database

- PostgreSQL

## Cache

- Redis

## Messaging

- Apache Kafka

## AI & Machine Learning

- Retrieval-Augmented Generation (RAG)
- FAISS Vector Search
- Groq LLM

## DevOps & Cloud

- Docker
- Docker Compose
- Kubernetes
- Helm
- Amazon Elastic Kubernetes Service (EKS)
- Amazon Elastic Container Registry (ECR)
- AWS Application Load Balancer (ALB)
- Prometheus
- Grafana
- Git
- GitHub

---

# Project Structure

```text
Enterprise-AI-KnowledgeOps-Platform
│
├── backend/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── public/
│   ├── nginx.conf
│   └── Dockerfile
│
├── k8s/
│   ├── deployments/
│   ├── services/
│   ├── ingress/
│   ├── configmaps/
│   └── secrets/
│
├── monitoring/
│
├── docker-compose.yml
├── README.md
├── .gitignore
└── LICENSE
```

---

# Workflow

1. User logs into the application.
2. User uploads PDF documents.
3. Backend publishes document processing events to Apache Kafka.
4. Kafka Consumer extracts document content.
5. FAISS generates vector embeddings.
6. Embeddings are stored for semantic retrieval.
7. User asks questions.
8. Relevant document chunks are retrieved.
9. Groq LLM generates intelligent responses.
10. Redis caches repeated responses for faster access.

---

# Kubernetes Components

The application is deployed on Amazon EKS using Kubernetes resources:

- Deployments
- Services
- ConfigMaps
- Secrets
- Persistent Volume Claims (PVC)
- Ingress
- Namespace Isolation

---

# Monitoring

Infrastructure monitoring is implemented using:

- Prometheus
- Grafana

The monitoring stack provides visibility into:

- Kubernetes Cluster Health
- Pod Status
- CPU Utilization
- Memory Utilization
- Node Metrics
- Workload Performance

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/dharshanworks/AI-KnowledgeOps-Platform.git
cd AI-KnowledgeOps-Platform
```

## Start Containers

```bash
docker compose up -d
```

## Stop Containers

```bash
docker compose down
```

---

# API Endpoints

| Endpoint | Description |
|----------|-------------|
| POST /register | User Registration |
| POST /login | User Login |
| POST /upload | Upload PDF |
| POST /chat | Ask Questions |
| GET /docs | Swagger Documentation |

---

# Local Services

| Service | URL |
|----------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |

---

# Screenshots

> Add screenshots after deployment.

- Login Page
- Dashboard
- PDF Upload
- AI Chat
- Kubernetes Pods
- Amazon EKS Deployment
- Grafana Dashboard
- Prometheus Metrics

---

# Future Enhancements

- GitOps using Argo CD
- Centralized Logging using Loki
- Horizontal Pod Autoscaling (HPA)
- Distributed Tracing
- GitHub Actions CI/CD Pipeline

---

# Project Highlights

- Enterprise-grade RAG Architecture
- AI-powered Knowledge Management Platform
- Event-Driven Processing with Apache Kafka
- Semantic Search using FAISS
- Groq LLM Integration
- Redis-based Response Caching
- Secure JWT Authentication
- Dockerized Microservices
- Kubernetes Deployment on Amazon EKS
- AWS ALB Ingress
- Infrastructure Monitoring with Prometheus & Grafana

---

# Skills Demonstrated

- Full Stack Development
- REST API Development
- AI & Retrieval-Augmented Generation (RAG)
- JWT Authentication
- Docker Containerization
- Kubernetes Orchestration
- Amazon EKS
- Amazon ECR
- AWS Networking
- Apache Kafka
- Redis
- PostgreSQL
- Prometheus Monitoring
- Grafana Dashboards
- Cloud Deployment

---

# Author

## Dharshan R

B.Tech Information Technology

Cloud & DevOps Enthusiast | Full Stack Developer | AI Engineer

- GitHub: https://github.com/dharshanworks
- LinkedIn: *(Add your LinkedIn Profile URL here)*

---

# License

This project is licensed under the MIT License.
