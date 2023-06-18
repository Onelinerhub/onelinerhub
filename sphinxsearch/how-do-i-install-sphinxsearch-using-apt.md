# How do I install SphinxSearch using APT?
// plain

1. To install SphinxSearch using APT, first add the SphinxSearch repository to the system:

```
$ sudo add-apt-repository ppa:builds/sphinxsearch-stable
```

2. Then update the package list:

```
$ sudo apt-get update
```

3. Finally install SphinxSearch:

```
$ sudo apt-get install sphinxsearch
```

4. After the installation is finished, the SphinxSearch binaries will be available in the `/usr/bin` directory.

5. To start the SphinxSearch service, use the `service` command:

```
$ sudo service sphinxsearch start
```

6. To check the status of the service, use the `status` command:

```
$ sudo service sphinxsearch status
```

7. To stop the service, use the `stop` command:

```
$ sudo service sphinxsearch stop
```

**Relevant Links**

- [SphinxSearch Documentation](https://sphinxsearch.com/docs/)
- [SphinxSearch Installation Guide](https://sphinxsearch.com/docs/current.html#installing)

onelinerhub: [How do I install SphinxSearch using APT?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-using-apt)