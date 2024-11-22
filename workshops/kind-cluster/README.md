# Create Kind Cluster
kind create cluster --config kind-config.yaml

# Set context to different namespace
kubectl config set-context --current --namespace <target_namespace> 

# Create a pod using kubectl
kubectl run nginx --image=nginx

# Describe a pod
kubectl describe pod nginx

# Delete a pod
kuebctl delete pod nginx

# Scale a deployment
kubectl scale deployment my app --replicas 4

# Update image in a deployment
kubectl set image deployment myapp myapp=nginx:1.10.1

# Check deployment rollout status
kubectl rollout status deployment/myapp

# Revert change from last deployment
kubectl rollout undo deployment/myapp

# Apply a Kube manifest
kubectl apply -f <file_name>

# Delete a Kube manifest
kubectl delete -f <file_name>

# Replace resources using a Kube manifest
kubectl replace -f <file_name>
