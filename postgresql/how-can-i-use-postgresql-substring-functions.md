# How can I use PostgreSQL substring functions?
// plain

PostgreSQL substring functions allow you to extract a substring from a string. The most commonly used substring functions are `substr`, `left`, `right`, and `substring`.

## Example code

```
SELECT substr('PostgreSQL', 6);
```
## Output example

```
SQL
```

The `substr` function takes two parameters: the string and the start position. It returns the substring starting from the start position to the end of the string.

The `left` function takes two parameters: the string and the number of characters to extract. It returns the leftmost substring of the specified length.

## Example code

```
SELECT left('PostgreSQL', 4);
```
## Output example

```
Post
```

The `right` function takes two parameters: the string and the number of characters to extract. It returns the rightmost substring of the specified length.

## Example code

```
SELECT right('PostgreSQL', 3);
```
## Output example

```
SQL
```

The `substring` function takes three parameters: the string, the start position, and the number of characters to extract. It returns the substring starting from the start position with the specified length.

## Example code

```
SELECT substring('PostgreSQL', 2, 5);
```
## Output example

```
ostG
```

For more information on PostgreSQL substring functions, see the [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-string.html).

onelinerhub: [How can I use PostgreSQL substring functions?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-substring-functions)