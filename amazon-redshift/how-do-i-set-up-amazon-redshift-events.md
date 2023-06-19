# How do I set up Amazon Redshift events?
// plain

Setting up Amazon Redshift events requires the following steps:

1. Create an Amazon Redshift cluster.
2. Create a database and schema in the cluster.
3. Create a table in the schema.
4. Create an Amazon EventBridge rule to trigger an event when the target table is modified.

## Example code

```
CREATE EVENT TRIGGER my_trigger
ON my_table
AFTER INSERT OR UPDATE OR DELETE
EXECUTE PROCEDURE my_procedure();
```

5. Create a stored procedure to handle the event.

## Example code

```
CREATE PROCEDURE my_procedure()
BEGIN
  -- Do something when the table is modified.
END;
```

6. Create an IAM role to allow Amazon EventBridge to invoke the stored procedure.
7. Test the event trigger by modifying the target table.

## Helpful links

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-triggers.html)
- [Creating an Event Trigger](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EVENT_TRIGGER.html)
- [Creating a Stored Procedure](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_PROCEDURE.html)

onelinerhub: [How do I set up Amazon Redshift events?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-redshift-events)