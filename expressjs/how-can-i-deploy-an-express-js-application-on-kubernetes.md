# How can I deploy an Express.js application on Kubernetes?
// plain

1. Create a Dockerfile that builds a Docker image for your Express.js application.

```
FROM node:10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

2. Build the Docker image and push it to a Docker registry.

```
docker build -t express-app .
docker tag express-app:latest <docker-registry>/express-app:latest
docker push <docker-registry>/express-app:latest
```

3. Create a Kubernetes deployment manifest file.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: express-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: express-app
  template:
    metadata:
      labels:
        app: express-app
    spec:
      containers:
        - name: express-app
          image: <docker-registry>/express-app:latest
          ports:
            - containerPort: 3000
```

4. Create a Kubernetes service manifest file.

```
apiVersion: v1
kind: Service
metadata:
  name: express-app
spec:
  type: NodePort
  selector:
    app: express-app
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
```

5. Deploy the application to Kubernetes.

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

6. Verify the deployment.

```
kubectl get pods
```

## Output example

```
NAME                              READY   STATUS    RESTARTS   AGE
express-app-7c8d7b6f9-x2lhb       1/1     Running   0          3m
```

7. Access the application.

The application will be accessible at `<node-ip>:<node-port>`.

## Helpful links

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- [Kubernetes deployment manifest reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#deployment-v1-apps)
- [Kubernetes service manifest reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#service-v1-core)
- [Kubernetes get pods reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.17/#get-pods-list-v1-core)

onelinerhub: [How can I deploy an Express.js application on Kubernetes?](https://onelinerhub.com/expressjs/how-can-i-deploy-an-express-js-application-on-kubernetes)