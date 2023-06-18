# How do I configure a SphinxSearch server?
// plain

1. Install SphinxSearch on the server. This can be done via a package manager like apt-get or yum, or manually from source.

2. Create a configuration file for SphinxSearch. This should include a data source definition, index definitions, searchd settings, and indexer settings. An example configuration file is shown below.

```
source mysource
{
    type            = mysql
    sql_host        = localhost
    sql_user        = root
    sql_pass        =
    sql_db          = test
    sql_port        = 3306  # optional, default is 3306
    sql_query_pre   = SET NAMES utf8
    sql_query_pre   = SET SESSION query_cache_type=OFF
    sql_query       = SELECT id, group_id, UNIX_TIMESTAMP(date_added) AS date_added, title, content FROM documents
}

index myindex
{
    source          = mysource
    path            = /var/data/myindex
    docinfo         = extern
    mlock           = 0
    morphology      = stem_en, soundex
    min_word_len    = 1
    charset_type    = utf-8
    charset_table   = 0..9, A..Z->a..z, _, a..z, U+C0..U+FF->U+E0..U+FF, U+410..U+42F->U+430..U+44F
}

searchd
{
    listen          = 127.0.0.1:9312
    log             = /var/log/searchd.log
    query_log       = /var/log/query.log
    read_timeout    = 5
    max_children    = 30
    pid_file        = /var/run/searchd.pid
    max_matches     = 1000
    seamless_rotate = 1
    preopen_indexes = 1
    unlink_old      = 1
    workers         = threads # for RT to work
}

```

3. Start the searchd daemon. This can be done using the command `searchd --config /path/to/sphinx.conf`.

4. Index the data source. This can be done using the command `indexer --config /path/to/sphinx.conf --all`.

5. Test the search server. This can be done using the command `search --config /path/to/sphinx.conf "search query"`.

6. Optimize the index. This can be done using the command `indexer --config /path/to/sphinx.conf --rotate --all`.

7. Setup a cron job to periodically re-index the data source.

## Helpful links
- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx Configuration Tutorial](http://sphinxsearch.com/docs/current.html#conf-overview)

onelinerhub: [How do I configure a SphinxSearch server?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-a-sphinxsearch-server)