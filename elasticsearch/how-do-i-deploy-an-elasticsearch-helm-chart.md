# How do I deploy an Elasticsearch Helm chart?
// plain

Deploying an Elasticsearch Helm chart is a simple process.

1. First, you need to add the Elastic Helm Chart repository to your local Helm instance by running the following command:

```
helm repo add elastic https://helm.elastic.co
```

2. Next, you need to update your local Helm repository by running the following command:

```
helm repo update
```

3. Then, you can install the Elasticsearch Helm chart by running the following command:

```
helm install my-release elastic/elasticsearch
```

4. You can then verify the installation by running the following command:

```
helm list
```

The output should look like this:

```
NAME            REVISION        UPDATED                         STATUS          CHART           APP VERSION     NAMESPACE
my-release      1               Thu Jul 30 10:29:43 2020        DEPLOYED        elasticsearch-7.7.1 7.7.1           default
```

5. Finally, you can access the Elasticsearch instance by running the following command:

```
kubectl get service
```

The output should look like this:

```
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
my-release      ClusterIP   10.43.246.129    <none>        9200/TCP   57s
```

## Helpful links

- [Elastic Helm Chart Repository](https://helm.elastic.co)
- [Helm Documentation](https://helm.sh/docs)
- [Kubernetes Documentation](https://kubernetes.io/docs)

onelinerhub: [How do I deploy an Elasticsearch Helm chart?](https://onelinerhub.com/elasticsearch/how-do-i-deploy-an-elasticsearch-helm-chart)