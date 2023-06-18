# How do I install SphinxSearch on Linux?
// plain

1. Download the latest version of SphinxSearch from its [download page](http://sphinxsearch.com/downloads/).
2. Extract the downloaded archive with the command: `tar -xzvf sphinx-<version>-release.tar.gz`
3. Change directory to the extracted directory: `cd sphinx-<version>-release`
4. Run the configuration script: `./configure`
5. Compile and install SphinxSearch with the command: `make && make install`
6. Start SphinxSearch server with the command: `searchd --config <config_file>`
7. Test the installation with the command: `search --config <config_file> test`

```
$ tar -xzvf sphinx-2.2.11-release.tar.gz
$ cd sphinx-2.2.11-release
$ ./configure
$ make && make install
$ searchd --config sphinx.conf
$ search --config sphinx.conf test
Sphinx 2.2.11-id64-release (r5654)
Copyright (c) 2001-2017, Andrew Aksyonoff
Copyright (c) 2008-2017, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file 'sphinx.conf'...
index 'test1': query 'test' retrieved 0 matches of 0 documents in 0.000 sec
```

onelinerhub: [How do I install SphinxSearch on Linux?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-linux-1687113151)