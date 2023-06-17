# How do I use an elasticsearch operator?
// plain

An elasticsearch operator is a tool that helps manage and automate the deployment of the elasticsearch cluster. It is used to simplify the process of deploying, managing and monitoring the elasticsearch cluster.

Here is an example of how to use the elasticsearch operator:

```
# Create the elasticsearch operator
$ kubectl apply -f https://github.com/elastic/cloud-on-k8s/releases/download/1.0.0-beta1/elasticsearch-operator.yaml

# Create the elasticsearch cluster
$ kubectl apply -f https://github.com/elastic/cloud-on-k8s/releases/download/1.0.0-beta1/quickstart-es-cluster.yaml
```

The first command creates the elasticsearch operator, which is responsible for managing and monitoring the elasticsearch cluster. The second command creates the elasticsearch cluster itself.

The output of the commands should look like this:

```
serviceaccount/elasticsearch-operator created
clusterrole.rbac.authorization.k8s.io/elasticsearch-operator created
clusterrolebinding.rbac.authorization.k8s.io/elasticsearch-operator created
deployment.apps/elasticsearch-operator created
service/elasticsearch-operator created
elasticsearch.elasticsearch.k8s.elastic.co/quickstart created
```

In summary, the steps to use an elasticsearch operator are:

1. Create the elasticsearch operator: `kubectl apply -f https://github.com/elastic/cloud-on-k8s/releases/download/1.0.0-beta1/elasticsearch-operator.yaml`
2. Create the elasticsearch cluster: `kubectl apply -f https://github.com/elastic/cloud-on-k8s/releases/download/1.0.0-beta1/quickstart-es-cluster.yaml`

For more information on using the elasticsearch operator, see the [elasticsearch operator documentation](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-operator.html).

onelinerhub: [How do I use an elasticsearch operator?](https://onelinerhub.com/elasticsearch/how-do-i-use-an-elasticsearch-operator)