# How to install Sphinxsearch in Docker?
// plain

1. Install Docker on your system.
2. Pull the Sphinxsearch image from Docker Hub.
```
docker pull sphinxsearch/sphinxsearch
```
3. Run the image with the following command:
```
docker run -d --name sphinxsearch -p 9306:9306 sphinxsearch/sphinxsearch
```
4. Check the status of the container with the following command:
```
docker ps
```
5. You can now connect to the Sphinxsearch instance using the port 9306.

Detailed explanation:

1. Install Docker on your system: Install Docker on your system to be able to run the Sphinxsearch image.

2. Pull the Sphinxsearch image from Docker Hub: Pull the Sphinxsearch image from Docker Hub using the following command:

```
docker pull sphinxsearch/sphinxsearch
```

3. Run the image: Run the image with the following command:

```
docker run -d --name sphinxsearch -p 9306:9306 sphinxsearch/sphinxsearch
```

4. Check the status of the container: Check the status of the container with the following command:

```
docker ps
```

5. Connect to the Sphinxsearch instance: You can now connect to the Sphinxsearch instance using the port 9306.

## Helpful links

- [Docker Hub - Sphinxsearch](https://hub.docker.com/r/sphinxsearch/sphinxsearch)
- [Docker Documentation - Get Started](https://docs.docker.com/get-started/)

group: docker

onelinerhub: [How to install Sphinxsearch in Docker?](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-in-docker)