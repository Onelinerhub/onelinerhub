# Example of docker-compose with sphinxsearch
// plain

This is an example of a `docker-compose.yml` file for running a SphinxSearch instance:

```
version: '3.7'

services:
  sphinxsearch:
    image: sphinxsearch/sphinxsearch
    ports:
      - "9306:9306"
    environment:
      SPHINX_CONFIG_TYPE: "master"
      SPHINX_CONFIG_MASTER_HOST: "sphinxsearch"
      SPHINX_CONFIG_MASTER_PORT: "9306"
      SPHINX_CONFIG_MASTER_USER: "sphinx"
      SPHINX_CONFIG_MASTER_PASS: "sphinx"
```

This example will create a SphinxSearch instance with the following configuration:

* `image`: The Docker image to use for the instance.
* `ports`: The port mapping for the instance.
* `environment`: The environment variables for the instance.

The output of this example will be a running SphinxSearch instance on port 9306.

## Helpful links

* [SphinxSearch Docker Image](https://hub.docker.com/r/sphinxsearch/sphinxsearch)
* [Docker Compose Documentation](https://docs.docker.com/compose/)

group: docker

onelinerhub: [Example of docker-compose with sphinxsearch](https://onelinerhub.com/sphinx-search/example-of-docker-compose-with-sphinxsearch)