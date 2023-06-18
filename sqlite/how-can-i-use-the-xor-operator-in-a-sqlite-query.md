# How can I use the XOR operator in a SQLite query?
// plain

The XOR operator in a SQLite query can be used to compare two expressions and return a result of TRUE when one expression is true and the other is false. The syntax for using the XOR operator is `expr1 XOR expr2`.

For example, the following query uses the XOR operator to compare two expressions:

```sql
SELECT 5 XOR 3;
```

The output of this query will be `TRUE` since 5 is greater than 3.

The parts of this query are as follows:

* `SELECT`: the keyword used to initiate a query
* `5`: the first expression to be compared
* `XOR`: the XOR operator
* `3`: the second expression to be compared

For more information on the XOR operator in SQLite, please refer to the [SQLite documentation](https://www.sqlite.org/lang_expr.html#xor).

onelinerhub: [How can I use the XOR operator in a SQLite query?](https://onelinerhub.com/sqlite/how-can-i-use-the-xor-operator-in-a-sqlite-query)