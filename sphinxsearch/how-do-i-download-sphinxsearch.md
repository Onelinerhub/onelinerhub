# How do I download SphinxSearch?
// plain

1. Download the latest version of SphinxSearch from the official website [sphinxsearch.com](https://sphinxsearch.com/downloads/).
2. Choose your operating system and download the appropriate package.
3. For example, if you are running Linux, you can download the tar.gz package.
4. Unpack the package using the following command:
```
tar xvfz sphinx-2.2.11-release.tar.gz
```
5. Change into the directory created by unpacking the package:
```
cd sphinx-2.2.11-release
```
6. Run the configuration script:
```
./configure
```
7. Once the configuration is complete, you can compile and install the package:
```
make && make install
```

The output should look like this:
```
...
Installing sphinx.conf to /usr/local/etc/sphinx.conf
Installing searchd to /usr/local/bin/searchd
Installing indexer to /usr/local/bin/indexer
Installing spelldump to /usr/local/bin/spelldump
Installing wordbreaker to /usr/local/bin/wordbreaker
Installing libsphinxclient.a to /usr/local/lib/libsphinxclient.a
Installing libsphinxclient.so.2.2.11 to /usr/local/lib/libsphinxclient.so.2.2.11
Installing libsphinxclient.so.2 to /usr/local/lib/libsphinxclient.so.2
Installing libsphinxclient.so to /usr/local/lib/libsphinxclient.so
```

onelinerhub: [How do I download SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-download-sphinxsearch)