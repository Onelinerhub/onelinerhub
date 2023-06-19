# How can I deploy an Express.js application on a Kubernetes cluster?
// plain

To deploy an Express.js application on a Kubernetes cluster, you need to create a Docker image that contains your application, and then deploy it to the cluster.

First, create a `Dockerfile` that describes the steps to build the image:
```
FROM node:alpine

WORKDIR /usr/app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

Then, build the image:
```
docker build -t my-express-app .
```

Next, push the image to a container registry, like Docker Hub:
```
docker push my-express-app
```

Finally, deploy the image to the Kubernetes cluster with a `Deployment` resource:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-express-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-express-app
  template:
    metadata:
      labels:
        app: my-express-app
    spec:
      containers:
        - name: my-express-app
          image: my-express-app
          ports:
            - containerPort: 3000
```

Once the deployment is complete, you can access the application from outside the cluster with a `Service` resource.

Parts of the code:
- `FROM node:alpine`: sets the base image for the Docker image
- `WORKDIR /usr/app`: sets the working directory for the Docker image
- `COPY package.json .`: copies the `package.json` file to the working directory
- `RUN npm install`: runs `npm install` to install the dependencies
- `COPY . .`: copies the application code to the working directory
- `EXPOSE 3000`: exposes port 3000 to the outside world
- `CMD ["npm", "start"]`: runs `npm start` to start the application
- `docker build -t my-express-app .`: builds the Docker image
- `docker push my-express-app`: pushes the Docker image to a container registry
- `apiVersion: apps/v1`: sets the Kubernetes API version
- `kind: Deployment`: specifies the type of resource
- `replicas: 3`: specifies the number of replicas
- `selector: matchLabels`: specifies the labels used to select the pods
- `template: metadata`: specifies the metadata for the pods
- `containers: name`: specifies the name of the container
- `image: my-express-app`: specifies the Docker image to use
- `ports: containerPort`: specifies the port to expose

## Helpful links
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Kubernetes Deployment Documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Service Documentation](https://kubernetes.io/docs/concepts/services-networking/service/)

onelinerhub: [How can I deploy an Express.js application on a Kubernetes cluster?](https://onelinerhub.com/expressjs/how-can-i-deploy-an-express-js-application-on-a-kubernetes-cluster)