# How do I use regular expressions with Amazon Redshift?
// plain

Regular expressions can be used with Amazon Redshift to search for and manipulate strings. The `regexp_substr()` and `regexp_replace()` functions are used to search for and manipulate strings with regular expressions.

For example, to search for the word "cat" in a string, the following code can be used:
```
SELECT regexp_substr('This is a sentence about cats', 'cat');
```
The output of this code will be:
```
cat
```

To replace the word "cat" in a string with the word "dog", the following code can be used:
```
SELECT regexp_replace('This is a sentence about cats', 'cat', 'dog');
```
The output of this code will be:
```
This is a sentence about dogs
```

The code above consists of the following parts:
- `regexp_substr()` and `regexp_replace()` are the functions used to search for and manipulate strings with regular expressions.
- The first argument passed to the function is the string to be searched.
- The second argument passed to the function is the regular expression pattern to be searched for.
- The third argument passed to the function (for `regexp_replace()`) is the string to replace the matching pattern with.

For more information about using regular expressions with Amazon Redshift, please visit the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_REGEXP_ functions.html).

onelinerhub: [How do I use regular expressions with Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-use-regular-expressions-with-amazon-redshift)