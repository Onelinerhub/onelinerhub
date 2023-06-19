# How do I set up replication in Amazon Redshift?
// plain

Setting up replication in Amazon Redshift requires the use of the `CREATE REPLICATION` command. The following example code creates a replication rule named `my_replication_rule` that replicates data from a source table named `my_source_table` to a target table named `my_target_table`:

```
CREATE REPLICATION RULE my_replication_rule
  TO TABLE my_target_table
  FROM (TABLE my_source_table
  EVERY 5 minutes);
```

## Code explanation


- `CREATE REPLICATION`: This is the command used to create a replication rule.
- `RULE my_replication_rule`: This is the name of the replication rule being created.
- `TO TABLE my_target_table`: This is the name of the target table that will receive the replicated data.
- `FROM (TABLE my_source_table`: This is the name of the source table from which the data will be replicated.
- `EVERY 5 minutes`: This is the frequency at which the replication will occur.

Once the replication rule has been created, the data will be replicated from the source table to the target table at the specified frequency.

## Helpful links

- [Amazon Redshift Documentation - Working with Replication Rules](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_REPLICATION_RULE.html)

onelinerhub: [How do I set up replication in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-replication-in-amazon-redshift)