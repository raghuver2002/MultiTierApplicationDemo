# Multi-Tier App using Docker Compose

This project demonstrates deploying a multi-tier web application using Docker Compose.

## Stack
- Frontend: React
- Backend: Flask
- Database: PostgreSQL

## Steps to Run

```bash
git clone <this-repo>
cd MultiTierApplicationDemo
docker-compose up --build -d

Then open http://<your-public-ip>:8080 in a browser.
---
After creating these files and folders, you can compress them into a ZIP archive using your system’s file manager or:

```bash
zip -r MultiTierApplicationDemo.zip MultiTierApplicationDemo/
