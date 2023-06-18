# How do I install Sphinx search on Ubuntu?
// plain

1. Download the latest version of Sphinx from the official website (http://sphinxsearch.com/downloads/release/).

2. Extract the downloaded tar file using the following command:
```
tar -xzvf sphinx-<version>.tar.gz
```

3. Go to the extracted directory and run the configuration script:
```
cd sphinx-<version>
./configure
```

4. After the configuration is done, run the make command to compile the source code:
```
make
```

5. Finally, install the Sphinx search engine using the following command:
```
make install
```

6. Once installation is complete, you can verify it by running the following command:
```
searchd --help
```

7. You can also refer to the official documentation for more information (http://sphinxsearch.com/docs/).

onelinerhub: [How do I install Sphinx search on Ubuntu?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinx-search-on-ubuntu)