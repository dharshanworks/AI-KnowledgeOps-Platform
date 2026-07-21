<div align="center">

# Enterprise AI KnowledgeOps Platform

An AI-powered Knowledge Management Platform that enables organizations to securely upload documents and receive intelligent, context-aware answers using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Kafka](https://img.shields.io/badge/Apache-Kafka-231F20)
![Redis](https://img.shields.io/badge/Redis-Cache-DC382D)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# Overview

Enterprise AI KnowledgeOps Platform is a scalable document intelligence system that allows users to upload PDF documents, securely manage knowledge, and ask natural language questions based on document content.

The platform leverages Retrieval-Augmented Generation (RAG) to retrieve relevant document context using semantic vector search and generate accurate responses with Large Language Models.

---

# Key Features

- Secure JWT Authentication
- PDF Document Upload
- Event-Driven Document Processing with Apache Kafka
- Retrieval-Augmented Generation (RAG)
- FAISS Semantic Vector Search
- AI-powered Question Answering using Groq LLM
- Redis Response Caching
- PostgreSQL Database
- Dockerized Multi-Service Architecture
- RESTful APIs using FastAPI

---

# System Architecture

```
                        +----------------------+
                        |      React UI        |
                        +----------+-----------+
                                   |
                            REST API Requests
                                   |
                        +----------v-----------+
                        |      FastAPI         |
                        +----------+-----------+
                                   |
        -----------------------------------------------------
        |                 |                |                |
        |                 |                |                |
        ▼                 ▼                ▼                ▼
 PostgreSQL           Redis Cache      Apache Kafka      Authentication
                                             |
                                             ▼
                                     Kafka Consumer
                                             |
                                             ▼
                                     PDF Processing
                                             |
                                             ▼
                                       FAISS Vector DB
                                             |
                                             ▼
                                         Groq LLM
                                             |
                                             ▼
                                       AI Response
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

## Database

- PostgreSQL

## Cache

- Redis

## Messaging

- Apache Kafka

## AI

- Retrieval-Augmented Generation (RAG)
- FAISS
- Groq LLM

## Authentication

- JWT Authentication

## DevOps

- Docker
- Docker Compose
- Git
- GitHub

---

# Project Structure

```
Enterprise-AI-KnowledgeOps-Platform
│
├── backend
│   ├── api
│   ├── services
│   ├── models
│   ├── database
│   ├── auth
│   └── Dockerfile
│
├── frontend
│   ├── src
│   ├── components
│   ├── pages
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .env
```

---

# Workflow

1. User logs into the platform.
2. User uploads PDF documents.
3. Kafka publishes document processing events.
4. Consumer extracts document content.
5. FAISS creates vector embeddings.
6. User asks questions.
7. Relevant document chunks are retrieved.
8. Groq LLM generates context-aware responses.
9. Redis caches repeated responses for improved performance.

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/yourusername/Enterprise-AI-KnowledgeOps-Platform.git
cd Enterprise-AI-KnowledgeOps-Platform
```

## Start Docker Containers

```bash
docker compose up -d
```

## Stop Containers

```bash
docker compose down
```

---

# Services

| Service | URL |
|----------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |

---

# Future Enhancements

- Kubernetes Deployment
- Amazon EKS
- Amazon ECR
- ArgoCD GitOps
- Prometheus Monitoring
- Grafana Dashboards
- Loki Log Aggregation
- Horizontal Pod Autoscaling
- CI/CD using GitHub Actions

---

# Project Highlights

- Enterprise-ready architecture
- Event-driven processing with Kafka
- Semantic search using FAISS
- AI-powered document intelligence
- Secure authentication
- Containerized deployment
- Scalable backend services

---

# Author

**Dharshan R**

B.Tech Information Technology

Cloud & DevOps Enthusiast | Full Stack Developer | AI Engineer

---

## License

This project is licensed under the MIT License.
