# How can I import data into a D3 JavaScript project?
// plain

To import data into a D3 JavaScript project, you can use the `d3.csv` or `d3.json` methods. These methods allow you to read in data from a .csv or .json file, respectively. For example, to read in a .csv file named `data.csv`:

```javascript
d3.csv("data.csv", function(data) {
  // Do something with the data
});
```

The `data` argument passed to the callback function contains the parsed data from the file.

You can also use the `d3.text` method to read in a text file. For example, to read in a .txt file named `data.txt`:

```javascript
d3.text("data.txt", function(data) {
  // Do something with the data
});
```

The `data` argument passed to the callback function contains the text from the file.

## Code explanation

- `d3.csv`: reads in a .csv file
- `d3.json`: reads in a .json file
- `d3.text`: reads in a text file
- `data` argument: contains the parsed data from the file

## Helpful links
- [d3.csv](https://github.com/d3/d3-fetch/blob/master/README.md#csv)
- [d3.json](https://github.com/d3/d3-fetch/blob/master/README.md#json)
- [d3.text](https://github.com/d3/d3-fetch/blob/master/README.md#text)

onelinerhub: [How can I import data into a D3 JavaScript project?](https://onelinerhub.com/javascript-d3/how-can-i-import-data-into-a-d--javascript-project)