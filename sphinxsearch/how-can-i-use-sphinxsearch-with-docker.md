# How can I use Sphinxsearch with Docker?
// plain

You can use Sphinxsearch with Docker by running a container with the Sphinxsearch image. For example, to start a Sphinxsearch container with port 9312 exposed, you can use the following command:

```
docker run -d -p 9312:9306 -e MYSQL_HOST=<mysql_host> -e MYSQL_USER=<mysql_user> -e MYSQL_PASSWORD=<mysql_password> sphinxsearch/sphinxsearch
```

This will start a Sphinxsearch container and expose port 9312.

The command consists of the following parts:
- `docker run`: the command to start a container
- `-d`: run the container in detached mode
- `-p 9312:9306`: expose port 9312 from the container to the host
- `-e MYSQL_HOST=<mysql_host>`: set the environment variable `MYSQL_HOST` to the value of `<mysql_host>`
- `-e MYSQL_USER=<mysql_user>`: set the environment variable `MYSQL_USER` to the value of `<mysql_user>`
- `-e MYSQL_PASSWORD=<mysql_password>`: set the environment variable `MYSQL_PASSWORD` to the value of `<mysql_password>`
- `sphinxsearch/sphinxsearch`: the image to use for the container

Once the container is running, you can connect to it using the SphinxQL protocol on port 9312.

## Helpful links
- [Docker Documentation](https://docs.docker.com/)
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)

onelinerhub: [How can I use Sphinxsearch with Docker?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-with-docker)