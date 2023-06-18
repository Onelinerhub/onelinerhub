# How can I configure SphinxSearch to work with MediaWiki?
// plain

1. Install SphinxSearch:
   ```
   $ apt-get install sphinxsearch
   ```
2. Create SphinxSearch configuration file:
   ```
   $ nano /etc/sphinxsearch/sphinx.conf
   ```
3. Add the following lines to the configuration file:
   ```
   source mediawiki
   {
      type            = mysql

      sql_host        = localhost
      sql_user        = <username>
      sql_pass        = <password>
      sql_db          = <database>
      sql_port        = 3306  # default

      sql_query       = \
        SELECT page_id, page_title, page_touched \
        FROM page

      sql_attr_uint       = page_id
      sql_attr_timestamp  = page_touched
   }
   ```
4. Index the data from the MediaWiki database:
   ```
   $ indexer --all --config /etc/sphinxsearch/sphinx.conf
   ```
5. Start the searchd daemon:
   ```
   $ searchd --config /etc/sphinxsearch/sphinx.conf
   ```
6. Connect to SphinxSearch by using a library such as SphinxQL:
   ```
   $ mysql -h127.0.0.1 -P9306
   ```
7. Execute the query to search the MediaWiki database:
   ```
   mysql> SELECT * FROM mediawiki WHERE MATCH('<query>');
   ```

## Helpful links

- [SphinxSearch Installation](http://sphinxsearch.com/docs/current.html#installing)
- [SphinxSearch Configuration](http://sphinxsearch.com/docs/current.html#conf-overview)
- [SphinxSearch Indexing](http://sphinxsearch.com/docs/current.html#indexing-overview)
- [SphinxSearch Querying](http://sphinxsearch.com/docs/current.html#querying-overview)

onelinerhub: [How can I configure SphinxSearch to work with MediaWiki?](https://onelinerhub.com/sphinxsearch/how-can-i-configure-sphinxsearch-to-work-with-mediawiki)