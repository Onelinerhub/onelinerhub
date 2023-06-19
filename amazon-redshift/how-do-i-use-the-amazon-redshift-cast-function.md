# How do I use the Amazon Redshift CAST function?
// plain

The Amazon Redshift CAST function is used to convert one data type to another. It takes an expression of any type and converts it to a specified data type.

For example, the following code block will convert the string '123' to an integer:

```
SELECT CAST('123' AS INTEGER)
```

The output of this code will be:

```
123
```

The code consists of two parts:
1. The expression to be converted, which in this case is the string '123'.
2. The data type to convert the expression to, which in this case is an INTEGER.

You can also use the CAST function to convert a timestamp to a date, or a double to a decimal, or any other conversion that is supported by Redshift.

For more information about the CAST function, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CAST_function.html).

onelinerhub: [How do I use the Amazon Redshift CAST function?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-cast-function)