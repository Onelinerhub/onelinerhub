# How to merge multiple files with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvstack`. `csvstack` can be used to merge multiple CSV files into a single file.

## Example code

```
csvstack file1.csv file2.csv file3.csv > merged.csv
```

## Output example

```
Merged file saved as merged.csv
```

## Code explanation

- `csvstack`: the command used to merge multiple CSV files
- `file1.csv`, `file2.csv`, `file3.csv`: the files to be merged
- `>`: the output operator, used to save the merged file as `merged.csv`

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvkit tutorial](https://www.dataquest.io/blog/csvkit-tutorial/)

onelinerhub: [How to merge multiple files with csvkit?](https://onelinerhub.com/csvkit/how-to-merge-multiple-files-with-csvkit)