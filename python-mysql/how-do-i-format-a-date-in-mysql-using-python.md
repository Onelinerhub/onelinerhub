# How do I format a date in MySQL using Python?
// plain

To format a date in MySQL using Python, you can use the `strftime()` function. This function takes a datetime object as an argument and returns a string representing the date in the specified format.

For example, to format a date in the `YYYY-MM-DD` format:

```
import datetime

date = datetime.datetime.now()
formatted_date = date.strftime("%Y-%m-%d")

print(formatted_date)
```

## Output example

```
2020-08-19
```

The code above first imports the `datetime` module, then creates a `datetime` object and assigns it to the `date` variable. The `strftime()` function is then called on the `date` variable, passing in the format string `"%Y-%m-%d"` as an argument. This format string specifies that the date should be formatted as `YYYY-MM-DD`. Finally, the `print()` function displays the formatted date.

The `strftime()` function has many different format specifiers that can be used to customize the output. For more information, see the [Python documentation](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).

onelinerhub: [How do I format a date in MySQL using Python?](https://onelinerhub.com/python-mysql/how-do-i-format-a-date-in-mysql-using-python)