# How do I use the CASE WHEN statement in Amazon Redshift?
// plain

The CASE WHEN statement is used to evaluate a set of conditions and return a result. It is similar to an IF-THEN-ELSE statement. In Amazon Redshift, the CASE WHEN statement is used to evaluate a set of conditions and return a result based on the conditions that are met.

For example, the following code will return either 'Pass' or 'Fail' depending on the value of the 'grade' column:
```
SELECT CASE WHEN grade >= 50 THEN 'Pass' ELSE 'Fail' END AS result
FROM table_name
```

The code consists of the following parts:
1. The `CASE` keyword, which starts the statement.
2. The `WHEN` keyword, which is followed by a condition.
3. The `THEN` keyword, which is followed by the result if the condition is met.
4. The `ELSE` keyword, which is followed by the result if the condition is not met.
5. The `END` keyword, which ends the statement.

For more information about the CASE WHEN statement in Amazon Redshift, please refer to the [documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CASE.html).

onelinerhub: [How do I use the CASE WHEN statement in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-case-when-statement-in-amazon-redshift)