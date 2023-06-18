# How do I install Sphinxsearch on Ubuntu?
// plain

1. Download the latest version of Sphinxsearch from [Sphinxsearch download page](http://sphinxsearch.com/downloads/).
2. Extract the tar file with the command ```tar xvfz sphinx-2.2.10-release.tar.gz```
3. Change directory to the extracted directory: ```cd sphinx-2.2.10-release/```
4. Configure the build: ```./configure```
5. Compile the sources: ```make```
6. Install Sphinxsearch: ```sudo make install```
7. Once installed, you can start the search daemon: ```searchd --config sphinx.conf```

## Helpful links

- [Sphinxsearch download page](http://sphinxsearch.com/downloads/)
- [Sphinxsearch documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How do I install Sphinxsearch on Ubuntu?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-ubuntu)