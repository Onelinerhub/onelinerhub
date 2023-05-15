# How to remove header with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV files. It can be used to remove headers from CSV files.

## Example code

```
csvcut -n file.csv
```

This command will print out the column numbers and names of the header row.

To remove the header, use the following command:
```
csvcut -H -c <column numbers> file.csv
```

Where `<column numbers>` is a comma-separated list of the column numbers that you want to keep.

For example, if you want to keep the first three columns, you would use:
```
csvcut -H -c 1,2,3 file.csv
```

This will output the CSV file without the header row.

## Helpful links

- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvcut documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html)

onelinerhub: [How to remove header with csvkit?](https://onelinerhub.com/csvkit/how-to-remove-header-with-csvkit)