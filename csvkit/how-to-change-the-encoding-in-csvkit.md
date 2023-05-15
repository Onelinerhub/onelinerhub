# How to change the encoding in csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used to change the encoding of a CSV file.

To change the encoding of a CSV file, use the `in2csv` command with the `--encoding` option. For example, to convert a CSV file from UTF-8 to Latin-1 encoding:

```
in2csv --encoding=latin-1 input.csv > output.csv
```

This will convert the input file `input.csv` from UTF-8 to Latin-1 encoding and save the output to `output.csv`.

The `in2csv` command has several other options that can be used to customize the output. For example, the `--no-inference` option can be used to disable type inference, and the `--sheet` option can be used to specify the sheet name when converting from an Excel file.

For more information, see the [csvkit documentation](https://csvkit.readthedocs.io/en/latest/).

onelinerhub: [How to change the encoding in csvkit?](https://onelinerhub.com/csvkit/how-to-change-the-encoding-in-csvkit)