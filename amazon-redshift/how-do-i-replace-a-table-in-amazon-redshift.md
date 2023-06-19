# How do I replace a table in Amazon Redshift?
// plain

To replace a table in Amazon Redshift, you can use the `CREATE TABLE AS` command. This command creates a new table with the same structure as the original table and inserts the data from the original table into the new table. The following example code creates a new table called `new_table` from an existing table called `old_table`:

```sql
CREATE TABLE new_table AS
SELECT *
FROM old_table;
```

This command will create a new table with the same structure as `old_table` and insert the data from `old_table` into `new_table`.

You can also use the `CREATE TABLE AS` command to replace a table with a modified version of the original table. The following example code creates a new table called `new_table` with modified data from an existing table called `old_table`:

```sql
CREATE TABLE new_table AS
SELECT col1, col2, col3
FROM old_table
WHERE col3 > 5;
```

This command will create a new table with the same structure as `old_table` but only include data where `col3` is greater than 5.

For more information on the `CREATE TABLE AS` command, you can refer to the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_AS.html).

onelinerhub: [How do I replace a table in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-replace-a-table-in-amazon-redshift)