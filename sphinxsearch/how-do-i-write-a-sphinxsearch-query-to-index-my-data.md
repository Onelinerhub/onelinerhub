# How do I write a Sphinxsearch query to index my data?
// plain

To write a Sphinxsearch query to index your data, you need to write a `conf` file. This file contains all the configuration parameters that control the indexing process. Below is an example of a `conf` file for indexing a MySQL table:

```
source src1
{
    type            = mysql
    sql_host        = localhost
    sql_user        = user
    sql_pass        = pass
    sql_db          = db_name
    sql_query       = \
        SELECT id, name, address \
        FROM table_name
    sql_attr_uint   = id
    sql_attr_string = name
    sql_attr_string = address
}

index idx1
{
    source          = src1
    path            = /var/lib/sphinxsearch/data/idx1
    docinfo         = extern
    mlock           = 0
    morphology      = stem_en
    min_word_len    = 1
}
```

This example configuration defines a source called `src1` which specifies the MySQL connection parameters, the query to execute, and the attributes to index. It also defines an index called `idx1` which specifies the source to use, the path to store the index files, and some other parameters.

To index the data, you can then run the `indexer` command:

```
indexer --config /path/to/conf/file --all
```

This command will read the configuration file and index the data according to the parameters specified.

The parts of the code and their explanation are as follows:
- `source src1`: This defines the source of the data to be indexed.
- `sql_host`: This specifies the hostname of the MySQL server.
- `sql_user`: This specifies the username to connect to the MySQL server.
- `sql_pass`: This specifies the password to connect to the MySQL server.
- `sql_db`: This specifies the database name to connect to.
- `sql_query`: This specifies the query to execute to retrieve the data to be indexed.
- `sql_attr_uint` and `sql_attr_string`: These specify the attributes to be indexed.
- `index idx1`: This defines the index to be created.
- `path`: This specifies the path to store the index files.
- `docinfo`: This specifies the type of document info to store.
- `mlock`: This specifies whether to lock the index files in memory.
- `morphology`: This specifies the type of morphology to use.
- `min_word_len`: This specifies the minimum word length to index.
- `indexer`: This is the command to run to index the data.

For more information about writing Sphinxsearch queries, see the [Sphinxsearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I write a Sphinxsearch query to index my data?](https://onelinerhub.com/sphinxsearch/how-do-i-write-a-sphinxsearch-query-to-index-my-data)