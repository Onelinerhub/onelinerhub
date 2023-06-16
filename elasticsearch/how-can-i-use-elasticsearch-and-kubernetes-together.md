# How can I use Elasticsearch and Kubernetes together?
// plain

Elasticsearch and Kubernetes can be used together to deploy and manage Elasticsearch clusters. Here is an example of how to deploy an Elasticsearch cluster on Kubernetes using the official Helm chart:

```
# Install the Elasticsearch Helm chart
helm install --name my-cluster elasticsearch elastic/elasticsearch

# Check the status of the cluster
kubectl get pods

# Output
NAME                            READY   STATUS    RESTARTS   AGE
my-cluster-master-0             1/1     Running   0          2m
my-cluster-master-1             1/1     Running   0          2m
my-cluster-master-2             1/1     Running   0          2m
my-cluster-data-0               1/1     Running   0          2m
my-cluster-data-1               1/1     Running   0          2m
my-cluster-data-2               1/1     Running   0          2m
my-cluster-coordinating-only-0  1/1     Running   0          2m
```

The code above:

1. Installs the Elasticsearch Helm chart to deploy an Elasticsearch cluster on Kubernetes.
2. Checks the status of the cluster by running `kubectl get pods`.

## Helpful links

- [Elasticsearch Helm Chart](https://github.com/elastic/helm-charts/tree/master/elasticsearch)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

onelinerhub: [How can I use Elasticsearch and Kubernetes together?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-and-kubernetes-together)