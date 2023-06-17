# How can I use PostgreSQL with Kubernetes?
// plain

PostgreSQL can be used with Kubernetes to manage stateful applications.

To use PostgreSQL with Kubernetes, you need to create a [Kubernetes StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) for the PostgreSQL instances. This StatefulSet will manage the PostgreSQL instances, ensuring that they remain running and that the data is persisted.

You can also use the [Kubernetes PostgreSQL Operator](https://github.com/zalando/postgres-operator) to manage PostgreSQL deployments. This operator simplifies the deployment and management of PostgreSQL clusters on Kubernetes.

Below is an example of a Kubernetes StatefulSet for PostgreSQL:

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  selector:
    matchLabels:
      app: postgres
  serviceName: postgres
  replicas: 1
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:latest
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_DB
          value: mydb
        - name: POSTGRES_USER
          value: myuser
        - name: POSTGRES_PASSWORD
          value: mypassword
        volumeMounts:
        - name: postgres-data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: postgres-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: my-storage-class
      resources:
        requests:
          storage: 1Gi
```

This example StatefulSet will create a single instance of PostgreSQL, with the database name, username, and password specified in the `env` section. The data will be stored in a [Kubernetes Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), and the storage class name for the volume is specified in the `storageClassName` field.

## Helpful links
- [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Kubernetes PostgreSQL Operator](https://github.com/zalando/postgres-operator)
- [Kubernetes Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

onelinerhub: [How can I use PostgreSQL with Kubernetes?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-with-kubernetes)