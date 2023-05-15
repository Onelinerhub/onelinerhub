# How to convert a csv file to tab delimited with csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. To convert a csv file to tab delimited with csvkit, the `csvformat` command can be used.

## Example code

```
csvformat -t input.csv > output.tsv
```

## Output example

```
column1	column2	column3
value1	value2	value3
```

## Code explanation

- `csvformat`: the command used to convert a csv file to tab delimited
- `-t`: the flag used to specify the output delimiter as tab
- `input.csv`: the input csv file
- `output.tsv`: the output tab delimited file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to convert a csv file to tab delimited with csvkit?](https://onelinerhub.com/csvkit/how-to-convert-a-csv-file-to-tab-delimited-with-csvkit)