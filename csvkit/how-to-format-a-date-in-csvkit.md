# How to format a date in csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the comma-separated values format. To format a date in csvkit, you can use the `csvformat` command. This command allows you to specify the date format you want to use.

For example, to format a date in the format `YYYY-MM-DD`, you can use the following command:

```
csvformat -d '%Y-%m-%d' input.csv
```

This will output the date in the following format:

```
2020-01-01
```

## Code explanation


- `csvformat`: The command used to format a date in csvkit.
- `-d`: The flag used to specify the date format.
- `'%Y-%m-%d'`: The date format used in this example, which is `YYYY-MM-DD`.
- `input.csv`: The name of the input CSV file.

## Helpful links

- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to format a date in csvkit?](https://onelinerhub.com/csvkit/how-to-format-a-date-in-csvkit)