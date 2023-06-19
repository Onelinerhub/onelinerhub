# How do I use AngularJS and Kendo Grid together?
// plain

Using AngularJS and Kendo Grid together requires a few steps.

1. Include the Kendo UI library in your project.

```<script src="https://kendo.cdn.telerik.com/2018.2.620/js/kendo.all.min.js"></script>```

2. Create a new Angular module, and include the Kendo UI directives in it.

```
angular.module('myApp', [ 'kendo.directives' ])
```

3. Add the kendo-grid directive in your HTML view.

```
<kendo-grid options="mainGridOptions"></kendo-grid>
```

4. Set the grid options in your controller or directive.

```
$scope.mainGridOptions = {
    dataSource: {
        type: "odata",
        transport: {
            read: "//demos.telerik.com/kendo-ui/service/Northwind.svc/Orders"
        },
        pageSize: 5
    },
    sortable: true,
    pageable: true
};
```

5. Run the application and you will see the Kendo Grid rendered with AngularJS.

You can find more information about using AngularJS and Kendo Grid together [here](https://docs.telerik.com/kendo-ui/knowledge-base/angular-kendo-grid).

onelinerhub: [How do I use AngularJS and Kendo Grid together?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-and-kendo-grid-together)