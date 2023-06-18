# How do I start using SphinxSearch?
// plain

1. To start using SphinxSearch, you will need to install the search engine software. You can download the software from the [SphinxSearch website](https://sphinxsearch.com/downloads/).

2. After downloading the software, you can install it by running the following command in the terminal:

```
$ ./configure
$ make
$ sudo make install
```

3. Once the installation is complete, you can start the search daemon by running the following command:

```
$ searchd --config /path/to/sphinx.conf
```

4. Next, you will need to create an index. You can do this by running the following command:

```
$ indexer --config /path/to/sphinx.conf --all
```

5. The indexer command will create the index files in the specified data directory.

6. Finally, you can use the SphinxSearch API to query the index. The API provides functions for searching, sorting, and filtering the data.

7. You can find more information about using SphinxSearch in the [official documentation](https://sphinxsearch.com/docs/).

onelinerhub: [How do I start using SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-start-using-sphinxsearch)