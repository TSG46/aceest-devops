# Submitted by Sai Ganesh T

### Roll No: 2025ht66021

---

# ACEest Fitness DevOps CI/CD Project

## Project Overview

This project demonstrates the implementation of a DevOps CI/CD pipeline for the ACEest Fitness application.

The goal of this assignment is to automate the software delivery pipeline using modern DevOps tools such as Git, Docker, GitHub Actions, and Jenkins.

---

## Technologies Used

* Python (Flask Web Framework)
* Git & GitHub
* Pytest (Automated Testing)
* Docker (Containerization)
* GitHub Actions (Continuous Integration)
* Jenkins (Build Automation)

---

## Application Description

The ACEest Fitness application is a simple Flask web service that provides endpoints to check system health and retrieve client workout program data.

Example endpoints:

* `/` → Application status
* `/health` → Health check endpoint
* `/clients` → Sample client fitness programs

---

## Running the Application Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open in browser:

http://localhost:5000

---

## Running Automated Tests

Run tests using pytest:

python -m pytest

Expected result:

All tests should pass successfully.

---

## Docker Containerization

Build Docker image:

docker build -t aceest-app .

Run Docker container:

docker run -p 5000:5000 aceest-app

Access application:

http://localhost:5000

---

## CI/CD Pipeline

The project implements a DevOps CI/CD pipeline.

### GitHub Actions CI

Whenever code is pushed to GitHub:

1. The repository is checked out
2. Python environment is prepared
3. Dependencies are installed
4. Automated tests are executed
5. Docker image is built

---

### Jenkins Integration

Jenkins pulls the latest code from GitHub and executes the following build steps:

* Install dependencies
* Run automated tests
* Build Docker container

---

## DevOps Pipeline Architecture

Developer → GitHub Repository → GitHub Actions CI → Automated Testing → Docker Build → Jenkins Build Pipeline

---

## Project Structure

ACEest-devops

app.py – Flask application
requirements.txt – Python dependencies
Dockerfile – Docker container configuration
tests/test_app.py – Automated tests
.github/workflows/main.yml – GitHub Actions CI pipeline
README.md – Project documentation

---

## Conclusion

This project demonstrates how DevOps practices such as version control, automated testing, containerization, and CI/CD pipelines can improve software delivery efficiency and reliability.
