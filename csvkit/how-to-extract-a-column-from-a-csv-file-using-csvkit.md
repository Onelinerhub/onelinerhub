# How to extract a column from a CSV file using csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used to extract a column from a CSV file.

## Example code

```
csvcut -c <column_name> <input_file.csv>
```

## Output example

```
column_name
value1
value2
value3
```

The code above extracts the column with the name `column_name` from the CSV file `input_file.csv`.

## Code explanation

- `csvcut`: the command to extract a column from a CSV file
- `-c`: the flag to specify the column to be extracted
- `<column_name>`: the name of the column to be extracted
- `<input_file.csv>`: the name of the CSV file from which the column is to be extracted

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to extract a column from a CSV file using csvkit?](https://onelinerhub.com/csvkit/how-to-extract-a-column-from-a-csv-file-using-csvkit)