# How to install Sphinxsearch in Docker?
// plain

1. Install Docker on your system.
2. Pull the Sphinxsearch image from Docker Hub.
```
docker pull macbre/sphinxsearch
```
3. Run the image with the following command:
```
docker run -d --name sphinxsearch -p 9306:9306 macbre/sphinxsearch
```
4. Check the status of the container with the following command:
```
docker ps
```
5. You can now connect to the Sphinxsearch instance using the port 9306.

## Helpful links

- [Docker Hub - Sphinxsearch](https://hub.docker.com/r/macbre/sphinxsearch)
- [Docker Documentation - Get Started](https://docs.docker.com/get-started/)

group: docker

onelinerhub: [How to install Sphinxsearch in Docker?
](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-in-docker)
