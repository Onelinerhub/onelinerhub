# How to set up SphinxSearch with Docker Compose?
// plain

1. First, install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).

2. Then, create a `docker-compose.yml` file with the following content:

```
version: '3.7'
services:
  sphinxsearch:
    image: sphinxsearch/sphinxsearch
    ports:
      - "9306:9306"
```

3. This will pull the latest version of the SphinxSearch image from Docker Hub and expose the SphinxSearch port on port 9306.

4. Next, run the following command to start the SphinxSearch container:

```
$ docker-compose up -d
```

5. This will start the SphinxSearch container in the background.

6. To verify that the SphinxSearch container is running, use the following command:

```
$ docker-compose ps
```

7. The output should look something like this:

```
        Name               Command             State                 Ports
------------------------------------------------------------------------------------------
sphinxsearch_sphinxsearch_1   /usr/bin/sphinxsearch   Up      0.0.0.0:9306->9306/tcp
```

## Helpful links
- [SphinxSearch Docker Hub](https://hub.docker.com/r/sphinxsearch/sphinxsearch)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

onelinerhub: [How to set up SphinxSearch with Docker Compose?](https://onelinerhub.com/sphinxsearch/how-to-set-up-sphinxsearch-with-docker-compose)