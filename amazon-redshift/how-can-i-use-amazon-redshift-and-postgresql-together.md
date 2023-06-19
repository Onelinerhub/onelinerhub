# How can I use Amazon Redshift and PostgreSQL together?
// plain

Amazon Redshift and PostgreSQL can be used together to create a powerful, cost-effective data warehouse. Redshift is an enterprise-level data warehouse solution that is optimized for large-scale data analysis, while PostgreSQL is an open-source relational database that is typically used as a back-end data store.

To use Amazon Redshift and PostgreSQL together, you can use a PostgreSQL foreign data wrapper (FDW) to connect to Redshift, allowing you to query Redshift data from within PostgreSQL. This allows you to combine the scalability of Redshift with the flexibility of PostgreSQL.

For example, the following code snippet can be used to create a foreign table in PostgreSQL that connects to an Amazon Redshift table:

```
CREATE FOREIGN TABLE redshift_table
(
    id integer,
    name character varying
)
SERVER redshift_server
OPTIONS (
    host 'redshift.example.com',
    port '5439',
    dbname 'redshift_db',
    user 'postgres',
    password 'password'
);
```

Once the foreign table has been created, you can query it from PostgreSQL as if it were a regular table:

```
SELECT * FROM redshift_table;
```

## Output example


```
 id |  name
----+--------
  1 | Alice
  2 | Bob
```

## Code explanation


- `CREATE FOREIGN TABLE`: This statement is used to create a foreign table in PostgreSQL.
- `redshift_table`: This is the name of the foreign table being created.
- `id` and `name`: These are the columns that will be part of the foreign table.
- `redshift_server`: This is the name of the foreign server that will be used to connect to the Amazon Redshift table.
- `host`, `port`, `dbname`, `user`, and `password`: These are the options used to connect to the Amazon Redshift table.

## Helpful links

- [PostgreSQL Foreign Data Wrapper Documentation](https://www.postgresql.org/docs/9.6/fdw.html)
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)

onelinerhub: [How can I use Amazon Redshift and PostgreSQL together?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-and-postgresql-together)