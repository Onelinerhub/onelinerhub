# How do I use Elastic APM with PHP in a Docker container?
// plain

Using Elastic APM with PHP in a Docker container is relatively easy. First, you need to install the [Elastic APM Agent](https://www.elastic.co/guide/en/apm/agent/php/current/index.html) and [Elastic APM PHP Agent](https://github.com/elastic/apm-agent-php) library in your Dockerfile.

```
FROM php:7.4-fpm

RUN apt-get update && apt-get install -y libzip-dev
RUN docker-php-ext-install zip

# Install the Elastic APM Agent
RUN curl -L -O https://download.elastic.co/apm/apm-agent/release/apt/pool/main/e/elastic-apm-agent/elastic-apm-agent_1.13.0_amd64.deb
RUN dpkg -i --force-confnew elastic-apm-agent_1.13.0_amd64.deb

# Install the Elastic APM PHP Agent
RUN curl -L -O https://github.com/elastic/apm-agent-php/releases/download/v1.13.0/elastic-apm-agent-php_1.13.0_amd64.deb
RUN dpkg -i --force-confnew elastic-apm-agent-php_1.13.0_amd64.deb
```

After the installation is complete, you need to configure the `elastic-apm-php` agent in `php.ini`:

```
[ElasticApm]
elastic_apm_server_url=http://apm-server:8200
elastic_apm_application_name=MyApp
elastic_apm_environment=production
```

Finally, you need to start the Elastic APM Agent in the `docker-compose.yml` file:

```
elastic-apm:
  image: docker.elastic.co/apm/apm-server:7.10.0
  environment:
    - setup.kibana.host=kibana:5601
  ports:
    - 8200:8200
```

After the configuration is complete, you can start the Docker container and Elastic APM Agent will automatically start collecting data from your PHP application.

## Helpful links
- [Elastic APM Agent](https://www.elastic.co/guide/en/apm/agent/php/current/index.html)
- [Elastic APM PHP Agent](https://github.com/elastic/apm-agent-php)

onelinerhub: [How do I use Elastic APM with PHP in a Docker container?](https://onelinerhub.com/php-elastica/how-do-i-use-elastic-apm-with-php-in-a-docker-container)