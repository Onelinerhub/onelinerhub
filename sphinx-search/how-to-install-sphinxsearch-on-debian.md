# How to install Sphinxsearch on Debian?
// plain

1. Install Sphinxsearch on Debian by running the following command:
```
sudo apt-get install sphinxsearch
```
2. After the installation is complete, you can start the Sphinxsearch service by running the following command:
```
sudo service sphinxsearch start
```
3. To configure Sphinxsearch, edit the configuration file located at `/etc/sphinxsearch/sphinx.conf`.
4. To index your data, run the following command:
```
indexer --all
```
5. To start the search daemon, run the following command:
```
searchd
```

## Helpful links
- [Sphinxsearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinxsearch Installation Guide](http://sphinxsearch.com/docs/current.html#installation)

group: install

onelinerhub: [How to install Sphinxsearch on Debian?](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-on-debian)