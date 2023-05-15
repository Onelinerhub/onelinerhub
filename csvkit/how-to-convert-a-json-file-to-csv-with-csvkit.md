# How to convert a json file to csv with csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used to convert a json file to csv with the following command:

```
in2csv filename.json > filename.csv
```

This will create a csv file with the same name as the json file.

## Code explanation


- `in2csv`: This is the command used to convert a json file to csv.
- `filename.json`: This is the name of the json file to be converted.
- `>`: This is the output redirection operator, which redirects the output of the command to the specified file.
- `filename.csv`: This is the name of the csv file to be created.

## Helpful links

- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvkit Tutorial](https://www.dataquest.io/blog/csvkit-tutorial/)

onelinerhub: [How to convert a json file to csv with csvkit?](https://onelinerhub.com/csvkit/how-to-convert-a-json-file-to-csv-with-csvkit)