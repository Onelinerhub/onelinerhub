# How do I configure SphinxSearch?
// plain

SphinxSearch is a powerful open source search engine that can be used to quickly locate information within a large data set. To configure SphinxSearch, you will need to create a configuration file and then use the `searchd` command to start the search daemon.

Example configuration file:

```
index test1
{
    source          = test1_src
    path            = /var/data/test1
    docinfo         = extern
    mlock           = 0
    morphology      = stem_en
    min_word_len    = 1
    charset_type    = utf-8
    charset_table   = 0..9, A..Z->a..z, _, a..z, U+A8->U+B8, U+B8->U+A8, U+C0..U+DF->U+E0..U+FF, U+E0..U+FF
}

indexer
{
    mem_limit       = 32M
}

searchd
{
    listen          = 9312
    log             = /var/log/searchd.log
    query_log       = /var/log/query.log
    read_timeout    = 5
    max_children    = 30
    pid_file        = /var/run/searchd.pid
    max_matches     = 1000
    seamless_rotate = 1
    preopen_indexes = 1
    unlink_old      = 1
}
```

Once the configuration file has been created, you can start the search daemon using the `searchd` command:

```
$ searchd --config /path/to/sphinx.conf
```

This will start the search daemon and it will be ready to accept search requests.

## Code explanation

- `index`: This section defines the index and its settings.
- `source`: This is the name of the source from which the index will be built.
- `path`: This is the path to the index data files.
- `docinfo`: This specifies whether the index should store document information in the index file or in an external file.
- `mlock`: This specifies whether the index should be locked in memory or not.
- `morphology`: This specifies the type of morphology to be used for the index.
- `min_word_len`: This specifies the minimum length of words that should be indexed.
- `charset_type`: This specifies the character set type to be used for the index.
- `charset_table`: This specifies the character set table to be used for the index.
- `indexer`: This section defines the indexer and its settings.
- `mem_limit`: This specifies the maximum amount of memory that the indexer should use.
- `searchd`: This section defines the search daemon and its settings.
- `listen`: This specifies the port on which the search daemon should listen for requests.
- `log`: This specifies the path to the log file for the search daemon.
- `query_log`: This specifies the path to the query log file for the search daemon.
- `read_timeout`: This specifies the maximum amount of time the search daemon should wait for a request.
- `max_children`: This specifies the maximum number of child processes that can be spawned by the search daemon.
- `pid_file`: This specifies the path to the PID file for the search daemon.
- `max_matches`: This specifies the maximum number of matches that should be returned by a search query.
- `seamless_rotate`: This specifies whether the search daemon should rotate the index without interrupting the search process.
- `preopen_indexes`: This specifies whether the search daemon should pre-open the indexes when it starts.
- `unlink_old`: This specifies whether the search daemon should unlink the old index files after the index has been rotated.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)
- [SphinxSearch Configuration Guide](http://sphinxsearch.com/docs/current.html#conf-overview)

onelinerhub: [How do I configure SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-1687107933)