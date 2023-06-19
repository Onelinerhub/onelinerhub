# How do I create a schema in Amazon Redshift?
// plain

Creating a schema in Amazon Redshift is a simple process. The following example code block shows how to create a simple schema with two tables:

```sql
CREATE SCHEMA IF NOT EXISTS myschema;

CREATE TABLE myschema.table1 (
   id INTEGER NOT NULL,
   name VARCHAR(20) NOT NULL
);

CREATE TABLE myschema.table2 (
   id INTEGER NOT NULL,
   description VARCHAR(100) NOT NULL
);
```

This code will create a schema called `myschema` with two tables, `table1` and `table2`. `table1` has two columns, `id` and `name`, while `table2` has two columns, `id` and `description`.

## Code explanation


1. `CREATE SCHEMA IF NOT EXISTS myschema;` - This creates a schema called `myschema` if it does not already exist.
2. `CREATE TABLE myschema.table1 (id INTEGER NOT NULL, name VARCHAR(20) NOT NULL);` - This creates a table called `table1` in the `myschema` schema with two columns, `id` and `name`.
3. `CREATE TABLE myschema.table2 (id INTEGER NOT NULL, description VARCHAR(100) NOT NULL);` - This creates a table called `table2` in the `myschema` schema with two columns, `id` and `description`.

For more information on creating schemas in Amazon Redshift, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_SCHEMA.html).

onelinerhub: [How do I create a schema in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-create-a-schema-in-amazon-redshift)