# How do I use the GETDATE function in Amazon Redshift?
// plain

The GETDATE function can be used in Amazon Redshift to return the current date and time. It takes no parameters and always returns the same value for each user session.

## Example code

```
SELECT GETDATE();
```

## Output example

```
2020-05-18 11:00:00
```

The code consists of:
- `SELECT`: This keyword is used to indicate that a query is to be executed.
- `GETDATE()`: This is the function that returns the current date and time.

## Helpful links
- [Amazon Redshift Documentation on GETDATE](https://docs.aws.amazon.com/redshift/latest/dg/r_GETDATE.html)

onelinerhub: [How do I use the GETDATE function in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-getdate-function-in-amazon-redshift)