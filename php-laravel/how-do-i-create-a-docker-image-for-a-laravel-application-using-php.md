# How do I create a Docker image for a Laravel application using PHP?
// plain

Creating a Docker image for a Laravel application using PHP is easy.

1. First, create a `Dockerfile` with the following content:

```
FROM php:7.2-apache

# Install dependencies
RUN apt-get update && apt-get install -y \
    libzip-dev \
    zip \
    unzip

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql zip

# Copy our application code
COPY . /var/www/html/

# Set the working directory
WORKDIR /var/www/html

# Expose port 80
EXPOSE 80
```

2. Then, build the image using the `docker build` command:

```
docker build -t laravel-app .
```

3. Finally, run the container:

```
docker run -d -p 80:80 laravel-app
```

The image should be now created and the Laravel application should be running.

Parts of the code explained:

* `FROM php:7.2-apache`: This line specifies the base image to use for the Docker image.
* `RUN apt-get update && apt-get install -y`: This command installs the necessary packages for the application.
* `RUN a2enmod rewrite`: This command enables the Apache mod_rewrite module.
* `RUN docker-php-ext-install pdo_mysql zip`: This command installs the PHP extensions needed for the application.
* `COPY . /var/www/html/`: This command copies the application code into the container.
* `WORKDIR /var/www/html`: This command sets the working directory for the container.
* `EXPOSE 80`: This command exposes port 80 to the host machine.

## Helpful links

* [Docker Documentation](https://docs.docker.com/)
* [Laravel Documentation](https://laravel.com/docs)

onelinerhub: [How do I create a Docker image for a Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-do-i-create-a-docker-image-for-a-laravel-application-using-php)