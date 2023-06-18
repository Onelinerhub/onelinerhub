# How do I install Sphinxsearch 3 on Ubuntu?
// plain

1. Download the latest version of Sphinxsearch from [Sphinxsearch official website](http://sphinxsearch.com/downloads/).
2. Extract the downloaded tar file using the command: `tar -xzvf sphinx-3.x.x-release.tar.gz`.
3. Change the directory to the extracted folder using the command: `cd sphinx-3.x.x-release`.
4. Run the configuration script using the command: `./configure`.
5. Install Sphinxsearch using the command: `make && make install`.
6. Start the search daemon using the command: `searchd --config /etc/sphinxsearch/sphinx.conf`.
7. Test the installation using the command: `search --config /etc/sphinxsearch/sphinx.conf test`.

```
$ tar -xzvf sphinx-3.x.x-release.tar.gz
$ cd sphinx-3.x.x-release
$ ./configure
$ make && make install
$ searchd --config /etc/sphinxsearch/sphinx.conf
$ search --config /etc/sphinxsearch/sphinx.conf test
Sphinx 3.0.3-release (r4487)
Copyright (c) 2001-2018, Andrew Aksyonoff
Copyright (c) 2008-2016, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/etc/sphinxsearch/sphinx.conf'...
index 'test': query 'test ': returned 0 matches of 0 total in 0.000 sec

```

onelinerhub: [How do I install Sphinxsearch 3 on Ubuntu?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch---on-ubuntu)