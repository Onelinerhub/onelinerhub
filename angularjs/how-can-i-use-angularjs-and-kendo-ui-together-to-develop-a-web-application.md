# How can I use AngularJS and Kendo UI together to develop a web application?
// plain

AngularJS and Kendo UI can be used together to develop a web application. The combination of these two frameworks provides a powerful toolset for creating rich, interactive web applications. To use these frameworks together, you need to include the required scripts and stylesheets for both frameworks.

```
<script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.7/angular.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/kendo-ui/2015.3.930/js/kendo.all.min.js"></script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/kendo-ui/2015.3.930/styles/kendo.common.min.css" />
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/kendo-ui/2015.3.930/styles/kendo.default.min.css" />
```

Once the necessary scripts and stylesheets are included, you can use the AngularJS directives to create Kendo UI widgets. For example, to create a Kendo UI Grid, you can use the `kendo-grid` directive:

```
<kendo-grid options="gridOptions"></kendo-grid>
```

The `gridOptions` can be set in the controller code, which will define the columns, data source, etc. of the Grid.

```
$scope.gridOptions = {
    dataSource: {
        data: [
            { name: "John Doe", age: 33 },
            { name: "Jane Doe", age: 27 }
        ]
    },
    columns: [
        { field: "name" },
        { field: "age" }
    ]
};
```

This will create a Kendo UI Grid with two columns and two rows of data.

## Helpful links

- [Kendo UI and AngularJS Integration](https://docs.telerik.com/kendo-ui/framework/angularjs/introduction)
- [Kendo UI Grid Directive](https://docs.telerik.com/kendo-ui/api/javascript/ui/grid#directive-kendo-grid)

onelinerhub: [How can I use AngularJS and Kendo UI together to develop a web application?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-and-kendo-ui-together-to-develop-a-web-application)