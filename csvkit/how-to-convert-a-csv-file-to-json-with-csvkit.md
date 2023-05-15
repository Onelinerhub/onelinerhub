# How to convert a csv file to json with csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used to convert a csv file to json.

## Example code

```
csvjson input.csv > output.json
```

## Output example

```
{
  "name": "John Doe",
  "age": "30",
  "city": "New York"
}
```

## Code explanation


1. csvjson: This is the command used to convert a csv file to json.
2. input.csv: This is the name of the csv file that needs to be converted.
3. output.json: This is the name of the json file that will be created after the conversion.

## Helpful links

1. [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)
2. [Convert CSV to JSON with csvkit](https://www.datacamp.com/community/tutorials/convert-csv-json-python)

onelinerhub: [How to convert a csv file to json with csvkit?](https://onelinerhub.com/csvkit/how-to-convert-a-csv-file-to-json-with-csvkit)