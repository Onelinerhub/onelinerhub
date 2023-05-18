# How to restart SphinxSearch?
// plain

To restart SphinxSearch, you can use the following command:

```
sudo service sphinxsearch restart
```

This will restart the SphinxSearch service. The output should look like this:

```
Restarting sphinxsearch: Sphinx 2.2.11-id64-release (r5343)
Copyright (c) 2001-2015, Andrew Aksyonoff
Copyright (c) 2008-2015, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/etc/sphinxsearch/sphinx.conf'...
indexing index 'test1'...
collected 0 docs, 0.0 MB
sorted 0.0 Mhits, 100.0% done
total 0 docs, 0 bytes
total 0.001 sec, 0 bytes/sec, 0.00 docs/sec
skipping non-plain index 'testrt'...
total 0 reads, 0.000 sec, 0.0 kb/call avg, 0.0 msec/call avg
total 0 writes, 0.000 sec, 0.0 kb/call avg, 0.0 msec/call avg
```

Alternatively, you can also use the following command to restart SphinxSearch:

```
/etc/init.d/sphinxsearch restart
```

This command will also restart the SphinxSearch service.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Installation Guide](http://sphinxsearch.com/docs/current.html#installation)

onelinerhub: [How to restart SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-restart-sphinxsearch)