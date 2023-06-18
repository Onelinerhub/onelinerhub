# How do I use ReactJS to generate an XLSX file?
// plain

Using ReactJS to generate an XLSX file is possible with the help of the npm package [js-xlsx](https://www.npmjs.com/package/xlsx). This package allows you to easily create and modify XLSX files with JavaScript.

To generate an XLSX file, you will need to create an array of objects with the data you want to include in the XLSX file. For example:

```
const data = [
  {
    name: 'John Doe',
    age: '30',
    city: 'New York'
  },
  {
    name: 'Jane Doe',
    age: '25',
    city: 'Los Angeles'
  }
]
```

Next, you will need to use the `writeFile` method from the `xlsx` package to generate the XLSX file. This method takes the data array and the file name as parameters. For example:

```
const XLSX = require('xlsx');
const fileName = 'people.xlsx';
XLSX.writeFile(data, fileName);
```

This code will generate a file called `people.xlsx` with the data from the array. The output of this code will be a file in the same directory where the code is located.

- `data`: an array of objects with the data that will be included in the XLSX file.
- `XLSX`: the `xlsx` package imported from npm.
- `fileName`: the name of the file that will be generated.
- `writeFile`: a method from the `xlsx` package that takes the data array and the file name as parameters and generates an XLSX file.

onelinerhub: [How do I use ReactJS to generate an XLSX file?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-to-generate-an-xlsx-file)