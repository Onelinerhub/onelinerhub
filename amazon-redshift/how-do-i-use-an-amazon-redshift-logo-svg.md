# How do I use an Amazon Redshift logo SVG?
// plain

Using an Amazon Redshift logo SVG requires a few steps.

1. Download the SVG file from the [Amazon Redshift logos page](https://aws.amazon.com/redshift/media/).

2. Include the SVG file within the HTML of the page you wish to use it on. This can be done by using the `<img>` tag, like so:

```
<img src="redshift_logo.svg" alt="Amazon Redshift Logo" width="200" height="50">
```

3. The SVG file can also be included in the CSS of the page, using the `background-image` property, like so:

```
.redshift-logo {
    background-image: url("redshift_logo.svg");
    width: 200px;
    height: 50px;
}
```

4. If you wish to manipulate the SVG file itself, you can use a library such as [Snap.svg](http://snapsvg.io/) to do so. For example, you could use the following code to change the color of the logo:

```javascript
var s = Snap("#redshift-logo");
s.select("#redshift-logo-path").attr({fill: "#009900"});
```

5. You can also use the SVG file in a JavaScript application. For example, you could use the [D3.js](https://d3js.org/) library to create a visualization with the logo:

```javascript
var svg = d3.select("#redshift-logo")
    .append("svg")
    .attr("width", 200)
    .attr("height", 50);

svg.append("image")
    .attr("xlink:href", "redshift_logo.svg")
    .attr("width", 200)
    .attr("height", 50);
```

These are just a few of the ways you can use an Amazon Redshift logo SVG.

onelinerhub: [How do I use an Amazon Redshift logo SVG?](https://onelinerhub.com/amazon-redshift/how-do-i-use-an-amazon-redshift-logo-svg)