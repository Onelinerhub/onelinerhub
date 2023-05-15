# How to reorder columns with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV files. It can be used to reorder columns in a CSV file.

## Example code

```
csvcut -c <columns> <input_file> | csvformat -T > <output_file>
```

## Output example

```
column1,column2,column3
value1,value2,value3
```

## Code explanation

- `csvcut`: used to select the columns to be included in the output file
- `-c`: used to specify the columns to be included in the output file
- `<columns>`: the list of columns to be included in the output file, separated by commas
- `<input_file>`: the path to the input CSV file
- `csvformat`: used to format the output file
- `-T`: used to output the file in tabular format
- `<output_file>`: the path to the output CSV file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to reorder columns with csvkit?](https://onelinerhub.com/csvkit/how-to-reorder-columns-with-csvkit)