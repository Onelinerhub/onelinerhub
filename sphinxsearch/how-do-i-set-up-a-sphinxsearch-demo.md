# How do I set up a SphinxSearch demo?
// plain

Setting up a SphinxSearch demo is a simple process.

1. Install the SphinxSearch software package by running the command:
```
sudo apt-get install sphinxsearch
```

2. Create a configuration file for your search index, using the command line tool `indexer`. For example:
```
indexer --config /etc/sphinxsearch/sphinx.conf --all
```

3. Create a data source for your search index, such as a MySQL database. For example:
```
mysql -u root -p
CREATE DATABASE sphinx_demo;
```

4. Import some data into your data source. For example:
```
mysql -u root -p sphinx_demo < /path/to/data.sql
```

5. Configure your SphinxSearch configuration file to use the data source. For example:
```
source src1
{
    type            = mysql
    sql_host        = localhost
    sql_user        = root
    sql_pass        = password
    sql_db          = sphinx_demo
    sql_query       = \
        SELECT id, title, content \
        FROM documents
}
```

6. Index your data source using the `indexer` command line tool. For example:
```
indexer --config /etc/sphinxsearch/sphinx.conf src1
```

7. Use the `search` command line tool to search your data source. For example:
```
search --config /etc/sphinxsearch/sphinx.conf "query"
```

This will set up a SphinxSearch demo.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)
- [SphinxSearch Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-ubuntu-14-04)

onelinerhub: [How do I set up a SphinxSearch demo?](https://onelinerhub.com/sphinxsearch/how-do-i-set-up-a-sphinxsearch-demo)