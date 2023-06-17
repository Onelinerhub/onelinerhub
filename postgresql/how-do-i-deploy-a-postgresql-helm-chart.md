# How do I deploy a PostgreSQL Helm chart?
// plain

1. First, add the official PostgreSQL chart repository to Helm: ```helm repo add bitnami https://charts.bitnami.com/bitnami```

2. Then, update the local Helm chart repository: ```helm repo update```

3. Next, install the PostgreSQL chart with a release name my-release: ```helm install my-release bitnami/postgresql```

4. The Helm chart will generate a set of Kubernetes resources including Deployment, Service, Secret and PersistentVolumeClaim.

5. It is possible to customize the installation by providing values to the chart. For example, to set the PostgreSQL root user password: ```helm install my-release bitnami/postgresql --set postgresqlRootPassword=secretpassword```

6. You can view the release details with: ```helm status my-release```

7. For more information, please visit the [official documentation](https://github.com/bitnami/charts/tree/master/bitnami/postgresql).

onelinerhub: [How do I deploy a PostgreSQL Helm chart?](https://onelinerhub.com/postgresql/how-do-i-deploy-a-postgresql-helm-chart)