# What are the system requirements for running Elasticsearch?
// plain

# System Requirements for running Elasticsearch

Elasticsearch requires **Java 8** or later in order to run. It is recommended to use the [OpenJDK](https://openjdk.java.net/) for running Elasticsearch.

In addition, the following system requirements must be met in order to run Elasticsearch:

- **Minimum of 2GB of memory** and **2 CPU cores**.
- **Minimum of 50GB of free disk space**.
- **Minimum of 1GB of swap space**.

For production deployments, it is recommended to use a minimum of 4GB of memory and 4 CPU cores, and at least 100GB of free disk space.

Below is an example of how to check the available memory on a Linux system:

```
$ free -m
              total        used        free      shared  buff/cache   available
Mem:           7862        6014         654          80        1193        1275
Swap:          2047           0        2047
```

The output above shows that the system has **7862MB** of RAM and **2047MB** of swap space.

For more information, please refer to the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html).

onelinerhub: [What are the system requirements for running Elasticsearch?](https://onelinerhub.com/elasticsearch/what-are-the-system-requirements-for-running-elasticsearch)