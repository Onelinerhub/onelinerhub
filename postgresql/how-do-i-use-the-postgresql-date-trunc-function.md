# How do I use the Postgresql date_trunc function?
// plain

The Postgresql `date_trunc` function is used to truncate a timestamp to a specified precision. It takes two arguments, a text string specifying the precision, and a timestamp.

For example, to truncate a timestamp to the nearest hour, you can use the following code:
```
SELECT date_trunc('hour', timestamp '2020-06-12 10:30:45');
```
The output of this query would be `2020-06-12 10:00:00`.

The precision argument can be one of the following values:
- `millennium`
- `century`
- `decade`
- `year`
- `quarter`
- `month`
- `week`
- `day`
- `hour`
- `minute`
- `second`

For example, to truncate a timestamp to the nearest day, you can use the following code:
```
SELECT date_trunc('day', timestamp '2020-06-12 10:30:45');
```
The output of this query would be `2020-06-12 00:00:00`.

## Helpful links
- [PostgreSQL Documentation - Date/Time Functions and Operators](https://www.postgresql.org/docs/current/functions-datetime.html)
- [PostgreSQL Documentation - Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html)

onelinerhub: [How do I use the Postgresql date_trunc function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-date-trunc-function)