# How do I install D3.js in my web project?
// plain

1. Download the latest version of D3.js from the official website [here](https://d3js.org/).
2. Unzip the downloaded file and save it in your project's directory.
3. Include the library in your HTML file:
```
<script src="path/to/d3.js"></script>
```
4. Create a new JavaScript file and reference it in your HTML file:
```
<script src="path/to/myScript.js"></script>
```
5. Start coding with D3.js in the newly created JavaScript file. Here is an example of a basic bar chart:
```
var data = [4, 8, 15, 16, 23, 42];

d3.select(".chart")
  .selectAll("div")
    .data(data)
  .enter().append("div")
    .style("width", function(d) { return d * 10 + "px"; })
    .text(function(d) { return d; });
```
6. The above code will generate a bar chart in a `<div>` element with the class `chart`.
7. For more information on how to use D3.js, check out the official documentation [here](https://github.com/d3/d3/wiki).

onelinerhub: [How do I install D3.js in my web project?](https://onelinerhub.com/javascript-d3/how-do-i-install-d--js-in-my-web-project)