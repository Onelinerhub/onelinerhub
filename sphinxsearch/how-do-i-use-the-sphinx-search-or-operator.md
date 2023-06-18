# How do I use the Sphinx search OR operator?
// plain

The Sphinx search OR operator is used to search for multiple words or phrases in a single query. It is used to perform a logical OR operation on a set of words or phrases.

For example, the following query:
```
SELECT * FROM table WHERE MATCH('word1 | word2')
```
will return all records from the table that contain either word1 or word2.

The OR operator can also be used in combination with the AND operator to perform a logical AND operation on multiple words or phrases. For example:
```
SELECT * FROM table WHERE MATCH('word1 | word2') AND MATCH('word3 | word4')
```
will return all records from the table that contain either word1 or word2 AND either word3 or word4.

The OR operator can also be used in combination with the NOT operator to perform a logical NOT operation on a set of words or phrases. For example:
```
SELECT * FROM table WHERE MATCH('word1 | word2') AND NOT MATCH('word3 | word4')
```
will return all records from the table that contain either word1 or word2 but do not contain either word3 or word4.

Here are some relevant links for more information:
- [Sphinx Search Documentation](http://sphinxsearch.com/docs/current.html)
- [Sphinx Search OR Operator](https://www.webhostinghero.com/how-to-use-the-sphinx-search-or-operator/)

onelinerhub: [How do I use the Sphinx search OR operator?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinx-search-or-operator)