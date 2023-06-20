# How can I create a Sankey diagram using D3.js and JavaScript?
// plain

A Sankey diagram is a type of flow diagram, in which the width of the arrows is proportional to the flow quantity. It can be created using D3.js and JavaScript.

To create a Sankey diagram, the following code can be used:
```
<script src="https://d3js.org/d3.v4.min.js"></script>
<script>
  var svg = d3.select("body").append("svg");
  var sankey = d3.sankey()
    .nodeWidth(15)
    .nodePadding(10)
    .extent([[1, 1], [width - 1, height - 6]]);

  var link = svg.append("g")
    .attr("class", "links")
    .attr("fill", "none")
    .attr("stroke", "#000")
    .attr("stroke-opacity", 0.2)
    .selectAll("path");

  var node = svg.append("g")
    .attr("class", "nodes")
    .attr("font-family", "sans-serif")
    .attr("font-size", 10)
    .selectAll("g");

  d3.json("energy.json", function(error, graph) {
    if (error) throw error;

    sankey(graph);

    link = link
      .data(graph.links)
      .enter().append("path")
      .attr("d", d3.sankeyLinkHorizontal())
      .attr("stroke-width", function(d) { return Math.max(1, d.width); });

    link.append("title")
      .text(function(d) { return d.source.name + " → " + d.target.name + "\n" + format(d.value); });

    node = node
      .data(graph.nodes)
      .enter().append("g");

    node.append("rect")
      .attr("x", function(d) { return d.x0; })
      .attr("y", function(d) { return d.y0; })
      .attr("height", function(d) { return d.y1 - d.y0; })
      .attr("width", function(d) { return d.x1 - d.x0; })
      .attr("fill", function(d) { return color(d.name.replace(/ .*/, "")); })
      .attr("stroke", "#000");

    node.append("text")
      .attr("x", function(d) { return d.x0 - 6; })
      .attr("y", function(d) { return (d.y1 + d.y0) / 2; })
      .attr("dy", "0.35em")
      .attr("text-anchor", "end")
      .text(function(d) { return d.name; })
      .filter(function(d) { return d.x0 < width / 2; })
      .attr("x", function(d) { return d.x1 + 6; })
      .attr("text-anchor", "start");

    node.append("title")
      .text(function(d) { return d.name + "\n" + format(d.value); });
  });
</script>
```

This code consists of the following parts:

1.  An SVG element is created and stored in a variable `svg`:
    ```
    var svg = d3.select("body").append("svg");
    ```

2. A Sankey layout is created and stored in a variable `sankey`:
    ```
    var sankey = d3.sankey()
      .nodeWidth(15)
      .nodePadding(10)
      .extent([[1, 1], [width - 1, height - 6]]);
    ```

3. The links and nodes of the Sankey diagram are created and stored in variables `link` and `node` respectively:
    ```
    var link = svg.append("g")
      .attr("class", "links")
      .attr("fill", "none")
      .attr("stroke", "#000")
      .attr("stroke-opacity", 0.2)
      .selectAll("path");

    var node = svg.append("g")
      .attr("class", "nodes")
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .selectAll("g");
    ```

4. The data for the Sankey diagram is retrieved from the `energy.json` file:
    ```
    d3.json("energy.json", function(error, graph) {
      if (error) throw error;
    ```

5. The Sankey layout is applied to the data:
    ```
    sankey(graph);
    ```

6. The links of the Sankey diagram are created and formatted:
    ```
    link = link
      .data(graph.links)
      .enter().append("path")
      .attr("d", d3.sankeyLinkHorizontal())
      .attr("stroke-width", function(d) { return Math.max(1, d.width); });

    link.append("title")
      .text(function(d) { return d.source.name + " → " + d.target.name + "\n" + format(d.value); });
    ```

7. The nodes of the Sankey diagram are created and formatted:
    ```
    node = node
      .data(graph.nodes)
      .enter().append("g");

    node.append("rect")
      .attr("x", function(d) { return d.x0; })
      .attr("y", function(d) { return d.y0; })
      .attr("height", function(d) { return d.y1 - d.y0; })
      .attr("width", function(d) { return d.x1 - d.x0; })
      .attr("fill", function(d) { return color(d.name.replace(/ .*/, "")); })
      .attr("stroke", "#000");

    node.append("text")
      .attr("x", function(d) { return d.x0 - 6; })
      .attr("y", function(d) { return (d.y1 + d.y0) / 2; })
      .attr("dy", "0.35em")
      .attr("text-anchor", "end")
      .text(function(d) { return d.name; })
      .filter(function(d) { return d.x0 < width / 2; })
      .attr("x", function(d) { return d.x1 + 6; })
      .attr("text-anchor", "start");

    node.append("title")
      .text(function(d) { return d.name + "\n" + format(d.value); });
    ```

This code will create a Sankey diagram based on the data in the `energy.json` file.

## Helpful links
- https://d3js.org/
- https://github.com/d3/d3-sankey

onelinerhub: [How can I create a Sankey diagram using D3.js and JavaScript?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-sankey-diagram-using-d--js-and-javascript)