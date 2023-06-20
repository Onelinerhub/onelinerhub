# How do I use different types of data with JavaScript and D3?
// plain

Using JavaScript and D3 together, you can create interactive data visualizations such as graphs, maps, and charts. To use different types of data with JavaScript and D3, you will need to convert the data into a format that D3 can read.

For example, to use a CSV file with D3, you can use the `d3.csv()` method to read the CSV file and return an array of objects.

```
d3.csv("data.csv", function(data){
  console.log(data);
});
```

This will output an array of objects, each object representing a row in the CSV file.

```
[
  {name: "Bob", age: 26},
  {name: "Alice", age: 24},
  {name: "John", age: 30}
]
```

Similarly, you can use the `d3.json()` method to read JSON data, the `d3.tsv()` method to read TSV data, and the `d3.html()` method to read HTML data.

Once the data is read and converted into an array of objects, you can use the data to create your visualization. For example, you can use the `d3.select()` method to select elements from the DOM and the `d3.enter()` method to add elements to the DOM, and use the data to determine the properties of the elements.

For more information on using data with D3, see the [D3 documentation](https://github.com/d3/d3/wiki/Tutorials).

onelinerhub: [How do I use different types of data with JavaScript and D3?](https://onelinerhub.com/javascript-d3/how-do-i-use-different-types-of-data-with-javascript-and-d-)