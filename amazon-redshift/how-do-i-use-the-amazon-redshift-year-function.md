# How do I use the Amazon Redshift YEAR function?
// plain

The YEAR function in Amazon Redshift is used to extract the year from a date value. It takes a single parameter, which is a date value, and returns an integer value for the year.

## Example code

```
SELECT YEAR('2020-08-21')
```

## Output example

```
2020
```

This example code takes the date value '2020-08-21' and returns the integer value for the year, which is 2020.

## Code explanation

1. `SELECT`: This keyword is used to retrieve data from the database.
2. `YEAR`: This is the function used to extract the year from a date value.
3. `'2020-08-21'`: This is the date value that is passed as the parameter to the YEAR function.

## Helpful links
- [Amazon Redshift Documentation - YEAR Function](https://docs.aws.amazon.com/redshift/latest/dg/r_YEAR.html)

onelinerhub: [How do I use the Amazon Redshift YEAR function?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-year-function)