# How to convert JSON to CSV using csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the king of tabular file formats. It can be used to convert JSON to CSV.

## Example code

```
csvjson myfile.json > myfile.csv
```

## Output example

```
id,name,age
1,John,20
2,Jane,30
3,Joe,40
```

The code above uses the csvjson command to convert a JSON file to a CSV file. The csvjson command takes a JSON file as input and outputs a CSV file.

## Code explanation

- csvjson: the command used to convert a JSON file to a CSV file
- myfile.json: the JSON file to be converted
- myfile.csv: the output CSV file

## Helpful links
- csvkit documentation: https://csvkit.readthedocs.io/en/latest/
- csvkit GitHub repository: https://github.com/wireservice/csvkit

onelinerhub: [How to convert JSON to CSV using csvkit?](https://onelinerhub.com/csvkit/how-to-convert-json-to-csv-using-csvkit)