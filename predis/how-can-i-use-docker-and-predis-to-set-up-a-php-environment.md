# How can I use Docker and Predis to set up a PHP environment?
// plain

To set up a PHP environment with Docker and Predis, you need to:

1. Create a `Dockerfile` with the following content:

```
FROM php:7.4-cli

RUN apt-get update && apt-get install -y \
    git \
    libpq-dev \
    && docker-php-ext-install pdo_pgsql

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer require predis/predis
```

2. Build the Docker image with the following command:

```
docker build -t <image-name> .
```

3. Run the Docker image with the following command:

```
docker run -it <image-name>
```

4. Test the installation of Predis by running the following code:

```
<?php

require 'vendor/autoload.php';

$client = new Predis\Client();
$client->set('foo', 'bar');
$value = $client->get('foo');

echo $value;

// Output: bar
```

## Helpful links
- [Docker Documentation](https://docs.docker.com/)
- [Predis Documentation](https://github.com/nrk/predis)

onelinerhub: [How can I use Docker and Predis to set up a PHP environment?](https://onelinerhub.com/predis/how-can-i-use-docker-and-predis-to-set-up-a-php-environment)