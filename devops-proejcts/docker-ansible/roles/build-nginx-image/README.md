# Ansible Role: Simple Nginx Docker

This Ansible role builds a Docker image called `simple-nginx` using a local `Dockerfile`, and runs a container from the image.

## ✅ Features

- Builds a custom Nginx Docker image using a provided `Dockerfile`.
- Runs the container and maps port 8080 to the container's port 80.
- Rebuilds the image and recreates the container if any changes are detected.