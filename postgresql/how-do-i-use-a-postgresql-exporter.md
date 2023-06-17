# How do I use a PostgreSQL exporter?
// plain

A PostgreSQL exporter is a tool used to export data from a PostgreSQL database. The exporter can be used to export data to a variety of formats, such as CSV, XML, JSON, and HTML.

The basic syntax of the PostgreSQL exporter is as follows:

```
\copy [table] to '[destination]' with [options];
```

Where:

* `[table]` is the name of the table you want to export.
* `[destination]` is the path to the file you are exporting to.
* `[options]` is an optional list of options that can be used to customize the output.

For example, to export the contents of the `users` table to a CSV file:

```
\copy users to 'users.csv' with (format csv, header true);
```

The output of this command would be a CSV file named `users.csv` containing the data from the `users` table.

For more information about the PostgreSQL exporter, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMANDS-COPY).

onelinerhub: [How do I use a PostgreSQL exporter?](https://onelinerhub.com/postgresql/how-do-i-use-a-postgresql-exporter)