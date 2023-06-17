# How do I set a timestamp in PostgreSQL?
// plain

PostgreSQL provides two timestamp data types: `timestamp` and `timestamptz`.

The `timestamp` data type stores the date and time information without any timezone information. The `timestamptz` data type stores the date and time information including the timezone information.

To set a timestamp in PostgreSQL, you can use the `to_timestamp` function.

For example, to set a `timestamp` with the value `2020-07-14 12:00:00`:
```
SELECT to_timestamp('2020-07-14 12:00:00', 'YYYY-MM-DD HH24:MI:SS');
```

## Output example

```
2020-07-14 12:00:00
```

To set a `timestamptz` with the value `2020-07-14 12:00:00`:
```
SELECT to_timestamp('2020-07-14 12:00:00', 'YYYY-MM-DD HH24:MI:SS')::timestamptz;
```

## Output example

```
2020-07-14 12:00:00+00
```

The `to_timestamp` function takes two parameters:
1. The timestamp value in `YYYY-MM-DD HH24:MI:SS` format.
2. The format of the timestamp value.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-formatting.html).

onelinerhub: [How do I set a timestamp in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-set-a-timestamp-in-postgresql)