# How can I use AngularJS to transform XLTS files?
// plain

AngularJS can be used to transform XLSX files by using the [SheetJS library](https://github.com/SheetJS/js-xlsx). SheetJS is an open source JavaScript library that allows developers to read and write XLSX files.

For example, the following code can be used to read an XLSX file and convert it into a JSON object:

```javascript
// Import the SheetJS library
const XLSX = require('xlsx');

// Read the XLSX file
const workbook = XLSX.readFile('sample.xlsx');

// Get the first worksheet
const worksheet = workbook.Sheets[workbook.SheetNames[0]];

// Convert the worksheet to a JSON object
const json = XLSX.utils.sheet_to_json(worksheet);

// Output the JSON object
console.log(json);
```

## Output example

```
[
  {
    "Name": "John",
    "Age": 20
  },
  {
    "Name": "Jane",
    "Age": 25
  }
]
```

The code above does the following:

1. Imports the SheetJS library (`const XLSX = require('xlsx');`).
2. Reads the XLSX file (`const workbook = XLSX.readFile('sample.xlsx');`).
3. Gets the first worksheet (`const worksheet = workbook.Sheets[workbook.SheetNames[0]];`).
4. Converts the worksheet to a JSON object (`const json = XLSX.utils.sheet_to_json(worksheet);`).
5. Outputs the JSON object (`console.log(json);`).

By using the SheetJS library, developers can easily transform XLSX files into JSON objects using AngularJS.

onelinerhub: [How can I use AngularJS to transform XLTS files?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-transform-xlts-files)