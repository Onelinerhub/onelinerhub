# How can I use SphinxSearch to search YouTube?
// plain

You can use SphinxSearch to search YouTube by using its [SphinxQL](http://sphinxsearch.com/docs/current.html#sphinxql-syntax) syntax.

For example, the following code block will search for videos with the keyword `cat`
```
SELECT * FROM videos WHERE MATCH('cat');
```

The output of this query will be a list of videos that contain the keyword `cat`:
```
+-------+---------+----------+
|   id  |  title  |  content |
+-------+---------+----------+
|  1    | Cat     | Cat video |
|  2    | Cat 2   | Cat video 2 |
|  3    | Cat 3   | Cat video 3 |
+-------+---------+----------+
```

The code block consists of the following parts:

- `SELECT *`: This is the SQL command that will be used to select all columns from the `videos` table.
- `FROM videos`: This specifies the table that SphinxSearch will search in.
- `WHERE MATCH('cat')`: This specifies the keyword that SphinxSearch will use to search for videos.

For more information on using SphinxSearch to search YouTube, please refer to the following links:

- [SphinxQL Syntax](http://sphinxsearch.com/docs/current.html#sphinxql-syntax)
- [Searching Data with SphinxSearch](https://www.digitalocean.com/community/tutorials/how-to-use-sphinx-to-search-data-on-a-vps)

onelinerhub: [How can I use SphinxSearch to search YouTube?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-to-search-youtube)