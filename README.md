## Boston ML App with Helm

```bash
helm install boston-ml-app helm-boston-ml-app/
helm status boston-ml-app
helm list
kubectl get pod -n boston
kubectl get svc -n boston
kubectl port-forward -n boston svc/boston-ml-app-nodeport 80:8000
```
