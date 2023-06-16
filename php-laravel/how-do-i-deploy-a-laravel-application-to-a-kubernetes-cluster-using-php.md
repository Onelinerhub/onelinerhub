# How do I deploy a Laravel application to a Kubernetes cluster using PHP?
// plain

Deploying a Laravel application to a Kubernetes cluster using PHP is a relatively straightforward process.

1. Create a Dockerfile for the application:

```
FROM php:7.4-fpm

RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip

RUN docker-php-ext-install pdo_mysql

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www/html

COPY . .

RUN composer install

CMD ["php-fpm"]
```

2. Build the Docker image:

```
docker build -t my-laravel-app .
```

3. Push the Docker image to a container registry:

```
docker push my-laravel-app
```

4. Create a Kubernetes deployment for the application:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-laravel-app
spec:
  selector:
    matchLabels:
      app: my-laravel-app
  replicas: 1
  template:
    metadata:
      labels:
        app: my-laravel-app
    spec:
      containers:
      - name: my-laravel-app
        image: my-laravel-app
        ports:
        - containerPort: 9000
```

5. Create a Kubernetes service for the application:

```
apiVersion: v1
kind: Service
metadata:
  name: my-laravel-app
spec:
  selector:
    app: my-laravel-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9000
```

6. Deploy the application to the cluster:

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

7. Access the application:

```
http://<KUBERNETES_IP>
```

## Helpful links

- [Deploying a Laravel Application to Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-laravel-application-to-kubernetes-on-ubuntu-18-04)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

onelinerhub: [How do I deploy a Laravel application to a Kubernetes cluster using PHP?](https://onelinerhub.com/php-laravel/how-do-i-deploy-a-laravel-application-to-a-kubernetes-cluster-using-php)