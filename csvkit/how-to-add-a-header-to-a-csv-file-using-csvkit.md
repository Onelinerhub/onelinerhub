# How to add a header to a CSV file using csvkit?
// plain

Adding a header to a CSV file using csvkit is a simple process.

## Example code

```
csvcut -n myfile.csv
csvcut -c 1,2,3 myfile.csv > newfile.csv
echo "header1,header2,header3" | cat - newfile.csv > temp.csv
mv temp.csv newfile.csv
```

## Output example

```
header1,header2,header3
data1,data2,data3
```

## Code explanation


1. `csvcut -n myfile.csv`: This command prints the column names of the CSV file.

2. `csvcut -c 1,2,3 myfile.csv > newfile.csv`: This command cuts the columns 1, 2 and 3 from the CSV file and stores them in a new file.

3. `echo "header1,header2,header3" | cat - newfile.csv > temp.csv`: This command adds the header to the new file and stores it in a temporary file.

4. `mv temp.csv newfile.csv`: This command moves the temporary file to the new file.

## Helpful links

- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvcut command](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html)

onelinerhub: [How to add a header to a CSV file using csvkit?](https://onelinerhub.com/csvkit/how-to-add-a-header-to-a-csv-file-using-csvkit)