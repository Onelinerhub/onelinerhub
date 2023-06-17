# How do I export data from PostgreSQL to an XML file?
// plain

Exporting data from PostgreSQL to an XML file can be done using the pg_dump utility. The following example code will export the table 'customers' from the database 'mydb' to an XML file named 'customers.xml':

```
pg_dump -U username -a -t customers -f customers.xml mydb
```

## Code explanation


- `pg_dump`: The utility used to export data from PostgreSQL
- `-U username`: The username to use when connecting to the database
- `-a`: Flag to include all table data
- `-t customers`: The name of the table to export
- `-f customers.xml`: The file name to export the data to
- `mydb`: The name of the database to export from

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/10/app-pgdump.html).

onelinerhub: [How do I export data from PostgreSQL to an XML file?](https://onelinerhub.com/postgresql/how-do-i-export-data-from-postgresql-to-an-xml-file)