# How can I use Kubernetes to deploy a React.js application?
// plain

Kubernetes can be used to deploy a React.js application with the following steps:

1. Create a Dockerfile for your React application. This will define the environment and dependencies your application needs to run.

```
FROM node:12.2.0-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]
```

2. Build a Docker image of your React application.

```
docker build -t my-react-app .
```

3. Create a Kubernetes deployment yaml file. This will define the number of replicas, ports, and other configurations for your application.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-react-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-react-app
  template:
    metadata:
      labels:
        app: my-react-app
    spec:
      containers:
      - name: my-react-app
        image: my-react-app
        ports:
        - containerPort: 3000
```

4. Create a Kubernetes service yaml file. This will define the type of service and port to use.

```
apiVersion: v1
kind: Service
metadata:
  name: my-react-app-service
spec:
  type: NodePort
  ports:
  - port: 3000
    nodePort: 30200
  selector:
    app: my-react-app
```

5. Deploy the React application to Kubernetes.

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

6. Access the application from your browser.

7. Monitor and manage the application using the Kubernetes dashboard.

## Helpful links
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Getting Started with Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Deploying a React Application to Kubernetes](https://medium.com/@james_aka_yale/deploying-a-react-application-to-kubernetes-8d4a7b8bd8d2)

onelinerhub: [How can I use Kubernetes to deploy a React.js application?](https://onelinerhub.com/reactjs/how-can-i-use-kubernetes-to-deploy-a-react-js-application)