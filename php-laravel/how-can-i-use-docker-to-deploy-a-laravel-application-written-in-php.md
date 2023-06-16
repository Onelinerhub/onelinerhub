# How can I use Docker to deploy a Laravel application written in PHP?
// plain

1. First, pull a Docker image from Docker Hub that contains the necessary components for running a Laravel application, such as an Apache web server and PHP. For example, `docker pull php:7.4-apache`.

2. Next, create a Dockerfile that will be used to build the container image for the Laravel application. The Dockerfile should include commands that copy the application files from the local filesystem into the image, install any necessary dependencies, and configure the web server.

3. Once the Dockerfile is created, build the container image using `docker build` command.

4. After the container image is built, create a container from the image using `docker run` command.

5. Finally, deploy the container to a server using `docker push` command.

6. After the container is deployed, it can be accessed by using the server's IP address or domain name.

7. To test the application, open a browser and enter the IP address or domain name of the server.

Example code block:
```
docker build -t laravel-app:1.0 .
```

## Output example

```
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM php:7.4-apache
 ---> 8f8f2f3f8bc3
Step 2/3 : COPY . /var/www/html
 ---> Using cache
 ---> 5a9b1fcaa8e2
Step 3/3 : RUN chown -R www-data:www-data /var/www/html
 ---> Running in aa9a3f9f7a7e
Removing intermediate container aa9a3f9f7a7e
 ---> 2f1e4f2f3f3f
Successfully built 2f1e4f2f3f3f
Successfully tagged laravel-app:1.0
```

## Code explanation

- `docker pull php:7.4-apache`: pull a Docker image from Docker Hub that contains the necessary components for running a Laravel application, such as an Apache web server and PHP.
- `docker build -t laravel-app:1.0 .`: build the container image for the Laravel application.
- `docker run`: create a container from the image.
- `docker push`: deploy the container to a server.

## Helpful links
- [Docker Hub](https://hub.docker.com/)
- [Docker Documentation](https://docs.docker.com/)

onelinerhub: [How can I use Docker to deploy a Laravel application written in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-docker-to-deploy-a-laravel-application-written-in-php)