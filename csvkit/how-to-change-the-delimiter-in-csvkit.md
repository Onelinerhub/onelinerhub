# How to change the delimiter in csvkit?
// plain

The delimiter in csvkit can be changed using the `csvformat` command.

## Example code

```
csvformat -D '|' input.csv > output.csv
```

This command will change the delimiter from the default comma (`,`) to a pipe (`|`) in the `input.csv` file and save the output to `output.csv`.

## Code explanation

- `csvformat`: the command used to change the delimiter
- `-D`: the flag used to specify the delimiter
- `'|'`: the delimiter to be used
- `input.csv`: the input file
- `output.csv`: the output file

## Helpful links
- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to change the delimiter in csvkit?](https://onelinerhub.com/csvkit/how-to-change-the-delimiter-in-csvkit)