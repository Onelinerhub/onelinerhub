# How do I use Amazon Redshift to perform an upsert operation?
// plain

Upsert is an operation that combines the Insert and Update operations. Amazon Redshift provides the `merge` command to perform an upsert operation.

The syntax of the `merge` command is as follows:
```
MERGE INTO target_table [alias]
USING source_table [alias]
ON target_table.key_column = source_table.key_column
WHEN MATCHED THEN
    UPDATE SET target_table.column1 = source_table.column1,
               target_table.column2 = source_table.column2,
               ...
WHEN NOT MATCHED THEN
    INSERT (column1, column2, ...)
    VALUES (source_table.column1, source_table.column2, ...)
```

The `merge` command combines the `update` and `insert` commands. It begins by specifying the target table and the source table. Then, it defines the `on` clause, which is used to match records from the source table and the target table. Next, it defines the `when matched` clause, which specifies the columns to be updated in the target table when a matched record is found. Finally, the `when not matched` clause is used to specify the columns to be inserted in the target table when a matched record is not found.

For example, the following `merge` command is used to upsert records from the `source_table` to the `target_table`:
```
MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET t.name = s.name,
               t.age = s.age
WHEN NOT MATCHED THEN
    INSERT (name, age)
    VALUES (s.name, s.age)
```

This command will update the `name` and `age` columns in the `target_table` when a matched record is found. Otherwise, it will insert a new record in the `target_table`.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_MERGE_command.html)

onelinerhub: [How do I use Amazon Redshift to perform an upsert operation?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-to-perform-an-upsert-operation)