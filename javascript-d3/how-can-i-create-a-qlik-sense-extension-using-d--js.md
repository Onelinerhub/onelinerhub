# How can I create a Qlik Sense Extension using D3.js?
// plain

Creating a Qlik Sense Extension using D3.js is relatively straightforward. It requires the following steps:

1. Create a Qlik Sense Extension object using the Qlik Sense Extension API.

```
var extension = {
    definition: {
        type: "items",
        component: "accordion",
        items: {
            settings: {
                uses: "settings"
            }
        }
    },
    paint: function () {
        // This is where the D3.js code will go
    }
};

```

2. Include the D3.js library in the extension.

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

3. Write the D3.js code within the paint function of the extension.

```
paint: function () {
    var data = [4, 8, 15, 16, 23, 42];

    d3.select("#myChart")
        .selectAll("div")
        .data(data)
        .enter()
        .append("div")
        .style("height", function(d) {
            var barHeight = d * 5;
            return barHeight + "px";
        });
}
```

4. Use the Qlik Sense Extension API to render the extension.

```
qlik.registerExtension("myExtension", extension);
```

The output of this code will be a bar chart rendered in the Qlik Sense app.

For more information, see the following links:
- [Qlik Sense Extension API](https://help.qlik.com/en-US/sense-developer/June2020/Subsystems/Extensions/Content/Sense_Extensions/extension-introduction.htm)
- [D3.js Documentation](https://github.com/d3/d3/wiki)

onelinerhub: [How can I create a Qlik Sense Extension using D3.js?](https://onelinerhub.com/javascript-d3/how-can-i-create-a-qlik-sense-extension-using-d--js)