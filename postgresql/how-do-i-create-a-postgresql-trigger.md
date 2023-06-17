# How do I create a PostgreSQL trigger?
// plain

Creating a trigger in PostgreSQL requires a few steps:
1. Create a function to execute when the trigger is fired. This function should accept the same parameters as the trigger.
```
CREATE FUNCTION my_trigger_function()
RETURNS trigger AS $$
BEGIN
    -- Your code goes here
END;
$$ LANGUAGE plpgsql;
```
2. Create the trigger itself, specifying the table and event it should fire on, as well as the function to execute.
```
CREATE TRIGGER my_trigger
AFTER INSERT ON my_table
FOR EACH ROW
EXECUTE PROCEDURE my_trigger_function();
```
3. Optionally, you can specify the timing of the trigger (BEFORE or AFTER) and the type of event (INSERT, UPDATE, or DELETE).

4. Optionally, you can also specify the conditions under which the trigger should fire using a `WHEN` clause.
```
CREATE TRIGGER my_trigger
AFTER INSERT ON my_table
FOR EACH ROW
WHEN (NEW.status = 'active')
EXECUTE PROCEDURE my_trigger_function();
```
5. Finally, you can enable and disable the trigger using the `ENABLE` and `DISABLE` commands, respectively.
```
ENABLE TRIGGER my_trigger ON my_table;
```

For more information, please see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-createtrigger.html).

onelinerhub: [How do I create a PostgreSQL trigger?](https://onelinerhub.com/postgresql/how-do-i-create-a-postgresql-trigger)