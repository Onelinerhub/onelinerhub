# How do I use the PostgreSQL to_char function?
// plain

The PostgreSQL `to_char` function is used to convert a timestamp or number into a string. The syntax of the `to_char` function is as follows:

```
to_char(value, format)
```

Where `value` is the timestamp or number to be converted and `format` is the format to use for the conversion.

For example, to convert a timestamp to a string with the format of 'DD-MON-YYYY' you would use the following:

```
SELECT to_char(current_timestamp, 'DD-MON-YYYY');
```

Which would output something like:

```
19-JAN-2021
```

The `format` argument can contain a wide variety of elements, including:

- `YYYY`: 4-digit year
- `MM`: 2-digit month
- `DD`: 2-digit day
- `HH24`: 24-hour format
- `MI`: Minute
- `SS`: Second

For a full list of available elements, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-formatting.html).

The `to_char` function is very useful when working with timestamps and numbers, allowing them to be easily converted into strings for display or other purposes.

onelinerhub: [How do I use the PostgreSQL to_char function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-to-char-function)