# Assessment Solutions

## Section 1: Kubernetes Concepts

### 1. Multiple Choice Questions
1. **c. Scheduler**
2. **c. To expose a stable network endpoint for Pods.**
3. **b. Secret**
4. **a. ClusterIP**
5. **b. Pod**

### 2. Short Answer Questions 
1. **Role of etcd in Kubernetes:**  
   etcd is a distributed key-value store used by Kubernetes to store all cluster state and configuration data reliably.

2. **What happens if a Pod in a Deployment crashes?**  
   Kubernetes automatically creates a new Pod to replace the crashed one, ensuring the desired state is maintained.

3. **Difference between ConfigMap and Secret:**  
   - ConfigMap stores non-sensitive configuration data.
   - Secret stores sensitive data, such as passwords or API keys, in an encrypted form.

4. **Why is Ingress preferred over NodePort for exposing services?**  
   Ingress provides more advanced features like routing rules, SSL termination, and load balancing, whereas NodePort directly exposes a service on a static port.

5. **Output of `kubectl get pods -o wide`:**  
   It displays additional information such as node name, IP address, and other metadata for each Pod.

---

## Section 2: Docker and Docker Compose Concepts

### 1. Fill-in-the-Blank Questions (5 points)
1. **docker-compose.yaml**
2. **docker build -t <image-name> .**
3. **all containers (running and stopped)**
4. **service dependencies**
5. **namespaces**

---

## Section 4: Advanced Docker and Kubernetes

### Kubernetes Troubleshooting

To debug a `CrashLoopBackOff` error, use the following commands:

- **`kubectl get pods`**: Check the status of the Pods to identify any failing instances.  
- **`kubectl logs <pod-name>`**: Retrieve the logs of the affected Pod to examine error messages.  
- **`kubectl describe pod <pod-name>`**: Get detailed information about the Pod, including events and configurations.  
- **`kubectl exec -it <pod-name> -- /bin/bash`**: Access the container interactively to investigate further issues.  
