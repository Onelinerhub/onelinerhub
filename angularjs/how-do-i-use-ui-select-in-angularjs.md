# How do I use ui-select in AngularJS?
// plain

UI-select is a directive for AngularJS that provides a select box with search functionality. It allows users to select multiple values from a list of options.

Using UI-select in AngularJS is simple and straightforward. Here's an example of how to use it:

```
<ui-select ng-model="selectedOption" theme="select2" ng-disabled="disabled">
  <ui-select-match placeholder="Select an option">{{$select.selected.name}}</ui-select-match>
  <ui-select-choices repeat="option in options | filter:$select.search">
    <div ng-bind-html="option.name | highlight: $select.search"></div>
  </ui-select-choices>
</ui-select>
```

This example code uses the `ui-select` directive to create a select box with search functionality. The `ng-model` attribute binds the selected option to the `selectedOption` variable. The `theme` attribute sets the theme of the select box, and the `ng-disabled` attribute can be used to disable the select box.

The `ui-select-match` directive defines the placeholder text for the select box. The `ui-select-choices` directive defines the list of options that can be selected. The `repeat` attribute defines the list of options to be used, and the `filter` attribute allows users to search for options. The `ng-bind-html` attribute binds the highlighted search results to the select box.

Here are some useful links for further reading:

- [UI-Select Documentation](https://github.com/angular-ui/ui-select)
- [AngularJS UI-Select Tutorial](https://www.c-sharpcorner.com/article/angular-js-ui-select-tutorial/)
- [UI-Select Examples](https://uiselect.github.io/examples.html)

onelinerhub: [How do I use ui-select in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-ui-select-in-angularjs)