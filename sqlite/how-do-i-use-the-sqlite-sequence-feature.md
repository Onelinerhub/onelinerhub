# How do I use the SQLite sequence feature?
// plain

The SQLite sequence feature allows you to create a unique sequence of numbers that can be used as an auto-incrementing primary key on a table. This is a useful feature for keeping track of items in a table or for generating unique values.

To use the SQLite sequence feature, you need to first create a sequence object using the `CREATE SEQUENCE` statement. For example:

```
CREATE SEQUENCE my_sequence;
```

You can then use the `NEXT VALUE FOR` statement to retrieve the next value in the sequence. For example:

```
SELECT NEXT VALUE FOR my_sequence;

-- Output:
1
```

You can also use `ALTER SEQUENCE` to modify the sequence object, such as changing the start value or the increment value. For example:

```
ALTER SEQUENCE my_sequence START WITH 10 INCREMENT BY 2;
```

The next time you use the `NEXT VALUE FOR` statement, it will start at 10 and increment by 2 each time.

Finally, you can use the `DROP SEQUENCE` statement to delete the sequence object.

For more information about using the SQLite sequence feature, please see the [SQLite documentation](https://www.sqlite.org/lang_createsequence.html).

onelinerhub: [How do I use the SQLite sequence feature?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-sequence-feature)