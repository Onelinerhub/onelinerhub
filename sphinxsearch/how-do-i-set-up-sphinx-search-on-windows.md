# How do I set up Sphinx search on Windows?
// plain

1. Download the latest version of Sphinx from [http://sphinxsearch.com/downloads/](http://sphinxsearch.com/downloads/).
2. Unzip the downloaded file.
3. Open the command line and navigate to the unzipped folder.
4. Run the configuration script with the following command:
```
./configure
```
5. Compile the source code with the following command:
```
make
```
6. Install the compiled binary with the following command:
```
make install
```
7. Start the Sphinx service with the following command:
```
searchd --config /path/to/sphinx.conf
```

## Helpful links

[http://sphinxsearch.com/docs/](http://sphinxsearch.com/docs/)

[https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04)

onelinerhub: [How do I set up Sphinx search on Windows?](https://onelinerhub.com/sphinxsearch/how-do-i-set-up-sphinx-search-on-windows)