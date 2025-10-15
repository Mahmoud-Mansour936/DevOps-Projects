# Production-Grade MongoDB Stack on Kubernetes

A sophisticated Kubernetes deployment demonstrating enterprise-level patterns including multi-namespace isolation, network security policies, persistent storage, and secrets management.

## Architecture Overview

This project implements a three-tier application across separate Kubernetes namespaces with strict security controls:

- **Namespace: `mongo-db`** - MongoDB database with persistent storage and network isolation
- **Namespace: `mongo-express`** - Database administration interface with controlled database access
- **Namespace: `fe`** - Front-end NGINX service with high availability (2 replicas)

## Key Security & Production Features

- **Network Isolation**: Kubernetes NetworkPolicy restricts database access to authorized namespaces only
- **Secret Management**: Sensitive credentials stored securely using Kubernetes Secrets
- **Persistent Storage**: MongoDB data persistence using PersistentVolumeClaims
- **Node Affinity**: Database pinned to specific node using `nodeName` and tolerations
- **Multi-Namespace Design**: Logical separation of concerns and access control
- **ConfigMap Configuration**: Externalized configuration for Mongo-Express

## Project Structure
├── db.yml # MongoDB deployment with PV, PVC, Secrets, NetworkPolicy
├── exp.yml # Mongo-Express deployment with ConfigMap
├── fe.yml # Front-end NGINX deployment
└── README.md


