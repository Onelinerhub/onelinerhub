# How do I round a number in PostgreSQL?
// plain

To round a number in PostgreSQL, you can use the round() function. This is a numeric function that takes two arguments: the number to be rounded and the number of decimal places to round it to.

For example, to round the number 3.14159 to two decimal places, you can use the following statement:

```
SELECT round(3.14159, 2);
```

The output of this statement will be:

```
 round
-------
  3.14
(1 row)
```

The round() function works by first rounding the number to the nearest integer. It then multiplies the result by 10 to the power of the number of decimal places specified. Finally, it divides the result by 10 to the power of the number of decimal places specified, resulting in the rounded number.

Here is a quick breakdown of the code:

- SELECT - returns the result of the expression
- round() - rounds the number to the specified number of decimal places
- 3.14159 - the number to be rounded
- 2 - the number of decimal places to round it to

For more information about the round() function, you can refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-math.html).

onelinerhub: [How do I round a number in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-round-a-number-in-postgresql)