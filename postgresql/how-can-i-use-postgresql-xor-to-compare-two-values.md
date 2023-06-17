# How can I use PostgreSQL XOR to compare two values?
// plain

PostgreSQL XOR is a logical operator used to compare two values. It returns true if one of the two values is true and the other is false. Otherwise, it returns false.

For example, the following code block uses PostgreSQL XOR to compare two values:

```
SELECT (1 = 1) XOR (2 = 3);
```

The output of this code is `true`.

The code can be broken down as follows:
- `SELECT`: This is the command used to retrieve data from the database.
- `(1 = 1) XOR (2 = 3)`: This is the logical expression used to compare the two values. `1 = 1` is true, whereas `2 = 3` is false. Since one of the two values is true and the other is false, the expression evaluates to true.

For more information, please refer to the following links:
- [PostgreSQL XOR](https://www.postgresqltutorial.com/postgresql-xor/)
- [PostgreSQL Logical Operators](https://www.postgresqltutorial.com/postgresql-logical-operators/)

onelinerhub: [How can I use PostgreSQL XOR to compare two values?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-xor-to-compare-two-values)