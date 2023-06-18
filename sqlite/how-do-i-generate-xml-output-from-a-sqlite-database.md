# How do I generate XML output from a SQLite database?
// plain

The easiest way to generate XML output from a SQLite database is to use the [sqlite3](https://www.sqlite.org/cli.html) command line tool. To generate XML output, the `.mode` command should be set to `xml` before running any SQL statements.

For example, the following code block will query the `Employees` table and generate XML output:

```
sqlite> .mode xml
sqlite> SELECT * FROM Employees;
<?xml version="1.0"?>
<resultset>
<row>
<ID>1</ID>
<Name>John Smith</Name>
<Age>32</Age>
</row>
<row>
<ID>2</ID>
<Name>Jane Doe</Name>
<Age>27</Age>
</row>
</resultset>
```

The code above consists of two parts:

1. The `.mode` command which sets the output format to XML.
2. The SQL query which retrieves the data from the `Employees` table.

For more information, please refer to the [SQLite documentation](https://www.sqlite.org/cli.html).

onelinerhub: [How do I generate XML output from a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-generate-xml-output-from-a-sqlite-database)