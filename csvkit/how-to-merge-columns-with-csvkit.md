# How to merge columns with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV files. It can be used to merge columns from multiple CSV files into a single file.

## Example code

```
csvstack -n 1,2,3 file1.csv file2.csv > merged.csv
```

## Output example

```
1,2,3
a,b,c
d,e,f
g,h,i
```

## Code explanation

- `csvstack`: the command to merge columns from multiple CSV files
- `-n 1,2,3`: the option to specify which columns to merge
- `file1.csv` and `file2.csv`: the two files to be merged
- `> merged.csv`: the output file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvkit tutorial](https://www.dataquest.io/blog/csvkit-tutorial/)

onelinerhub: [How to merge columns with csvkit?](https://onelinerhub.com/csvkit/how-to-merge-columns-with-csvkit)