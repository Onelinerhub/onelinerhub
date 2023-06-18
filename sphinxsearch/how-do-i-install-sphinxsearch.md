# How do I install SphinxSearch?
// plain

1. Download and install the [latest version of SphinxSearch](http://sphinxsearch.com/downloads/).
2. Extract the contents of the tarball to a directory of your choice.
3. Change directory to the extracted SphinxSearch directory.
4. Run the `./configure` script to configure the build process.
5. Run `make` to build SphinxSearch.
6. Run `make install` to install SphinxSearch.
7. Start the SphinxSearch daemon with the command `searchd --config <config_file>`.

Example code block:
```
tar -xzf sphinx-2.2.11-release.tar.gz
cd sphinx-2.2.11-release
./configure
make
make install
searchd --config sphinx.conf
```

Output of example code block:
```
searchd: listening on all interfaces, port=9312.
```

onelinerhub: [How do I install SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch)