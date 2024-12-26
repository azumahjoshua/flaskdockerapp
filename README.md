## **Deploying a Python Application using Docker and Kubernetes**

This project demonstrates how to containerize a Python application and deploy it to a Kubernetes cluster.

### **Steps to Deploy**

#### **1. Using Docker Compose**
To build and run the application locally using Docker Compose, use the following command:
```bash
docker-compose up --build -d
```

This will:
- Build the Docker image for the Python Flask application.
- Start the application along with a Redis service.

#### **2. Deploying to Kubernetes**
To deploy the application in a Kubernetes cluster, apply the YAML configuration files:
```bash
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
```

#### **3. Accessing the Application**
If you are using Minikube, you can find the external URL of your application with the following command:
```bash
minikube service flask-app-service
```

#### **4. Testing the Application**
You can access the application via a browser or test it using `curl`:
```bash
curl $(minikube service flask-app-service --url)
```

---

### **Project Overview**
- **Python Application:** A simple Flask application that increments a counter stored in Redis.
- **Redis Backend:** Used to persist the counter values.
- **Docker Compose:** For local development and testing.
- **Kubernetes Deployment:** For production-level orchestration.
