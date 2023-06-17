# How do I deploy Elasticsearch on Kubernetes?
// plain

1. **Create a Kubernetes cluster**: The first step is to create a Kubernetes cluster. This can be done using the `kubectl create cluster` command.

2. **Install Helm**: Helm is a package manager for Kubernetes and is needed to install the Elasticsearch Helm chart. Helm can be installed using the command `helm init`.

3. **Install the Elasticsearch Helm chart**: The Elasticsearch Helm chart can be installed using the command `helm install stable/elasticsearch`. This will create a deployment with the necessary components for running Elasticsearch on Kubernetes.

4. **Configure the Elasticsearch deployment**: The configuration for the Elasticsearch deployment can be done using a `values.yaml` file. This file can be used to configure the number of replicas, memory and CPU limits, and other settings.

5. **Create a service for the Elasticsearch deployment**: The Elasticsearch deployment needs to be exposed to the outside world. This can be done by creating a service using the command `kubectl expose deployment <deployment-name> --type=LoadBalancer`.

6. **Verify the deployment**: Once the deployment is complete, it can be verified using the command `kubectl get pods`. This will list all the pods that have been created for the Elasticsearch deployment.

7. **Access the Elasticsearch cluster**: After the deployment is complete, the Elasticsearch cluster can be accessed using the service endpoint.

```
curl http://<service-endpoint>:9200
```

## Output example

```
{
  "name" : "elasticsearch-cluster",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "abc123",
  "version" : {
    "number" : "7.0.0",
    ...
  },
  ...
}
```

## Code explanation
**

- `kubectl create cluster`: This command creates a Kubernetes cluster.
- `helm init`: This command installs Helm, a package manager for Kubernetes.
- `helm install stable/elasticsearch`: This command installs the Elasticsearch Helm chart.
- `values.yaml`: This file is used to configure the Elasticsearch deployment.
- `kubectl expose deployment <deployment-name> --type=LoadBalancer`: This command creates a service for the Elasticsearch deployment.
- `kubectl get pods`: This command lists all the pods that have been created for the Elasticsearch deployment.
- `curl http://<service-endpoint>:9200`: This command accesses the Elasticsearch cluster.

**## Helpful links**
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Helm Documentation](https://helm.sh/docs/)
- [Elasticsearch Helm Chart Documentation](https://github.com/elastic/helm-charts/tree/master/elasticsearch)

onelinerhub: [How do I deploy Elasticsearch on Kubernetes?](https://onelinerhub.com/elasticsearch/how-do-i-deploy-elasticsearch-on-kubernetes)