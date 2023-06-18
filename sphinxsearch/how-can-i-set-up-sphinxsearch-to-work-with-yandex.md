# How can I set up SphinxSearch to work with Yandex?
// plain

You can set up SphinxSearch to work with Yandex by following these steps:

1. Install SphinxSearch on your server.
2. Create a configuration file for the search index.
```
index test1
{
    source          = test1_src
    path            = /var/lib/sphinxsearch/data/test1
    docinfo         = extern
    mlock           = 0
    morphology      = stem_en, soundex
    min_word_len    = 2
    charset_type    = utf-8
    charset_table   = 0..9, A..Z->a..z, _, a..z, U+410..U+42F->U+430..U+44F, U+430..U+44F
}
```
3. Create a source file for the search index.
```
source test1_src
{
    type            = mysql
    sql_host        = localhost
    sql_user        = username
    sql_pass        = password
    sql_db          = test1
    sql_port        = 3306  # optional, default is 3306
    sql_query_pre   = SET NAMES utf8
    sql_query       = SELECT id, title, content FROM documents
    sql_attr_uint   = gid
}
```
4. Run the indexer to build the search index.
```
indexer --all
```
5. Start the search daemon.
```
searchd
```
6. Query the index using the SphinxSearch API.
```
$client = new SphinxClient();
$client->SetServer('localhost', 9312);
$client->SetMatchMode(SPH_MATCH_EXTENDED);
$client->Query('search query');
```
7. Finally, you can integrate the search results with Yandex.

## Helpful links
- [SphinxSearch Documentation](https://sphinxsearch.com/docs/current.html)
- [Yandex Documentation](https://yandex.ru/support/webmaster/search-engines/indexing.html)

onelinerhub: [How can I set up SphinxSearch to work with Yandex?](https://onelinerhub.com/sphinxsearch/how-can-i-set-up-sphinxsearch-to-work-with-yandex)