# How do I use the SQLite YEAR function?
// plain

The SQLite YEAR function is used to extract the year from a date value. It takes a single argument, which must be a valid date value. The output is an integer value representing the year.

For example:
```
SELECT YEAR('2019-11-02');
```
## Output example

```
2019
```

The code above uses the YEAR function to extract the year from the date value '2019-11-02'. The output is the integer value 2019.

The YEAR function can also be used in combination with other date functions to extract more specific information. For example, the following code will extract the year from the current date:
```
SELECT YEAR(CURRENT_DATE);
```

## Code explanation

- SELECT: the keyword used to retrieve data from the database
- YEAR(): the function used to extract the year from a date value
- '2019-11-02': the argument passed to the YEAR function, representing a valid date value
- Output: the integer value representing the year extracted from the date value
- CURRENT_DATE: the function used to get the current date

## Helpful links
- [SQLite Documentation](https://sqlite.org/lang_datefunc.html)
- [W3Schools SQLite Tutorial](https://www.w3schools.com/sql/sql_syntax.asp)

onelinerhub: [How do I use the SQLite YEAR function?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-year-function)