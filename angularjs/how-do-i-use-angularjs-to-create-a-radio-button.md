# How do I use AngularJS to create a radio button?
// plain

To create a radio button in AngularJS, you can use the `<input>` element with its `type` attribute set to `"radio"`. The `<input>` element should also have the `ng-model` attribute set to a variable that will store the value of the selected radio button.

```
<input type="radio" ng-model="selectedRadioButton" value="1">
```

The `value` attribute should be set to the value that will be stored in the variable when the radio button is selected.

In order to display the radio buttons in a group, they should be wrapped in a `<div>` element with the `ng-repeat` attribute set to loop through an array of values.

```
<div ng-repeat="radioButtonValue in radioButtonValues">
    <input type="radio" ng-model="selectedRadioButton" value="{{radioButtonValue}}">
</div>
```

The `ng-repeat` attribute will loop through the `radioButtonValues` array and create a new radio button for each value in the array. The `value` attribute of each `<input>` element will be set to the value of the current item in the array.

Finally, the `selectedRadioButton` variable can be used to get the value of the selected radio button.

## Helpful links
- [AngularJS ng-repeat Directive](https://www.w3schools.com/angular/ng_ng-repeat.asp)
- [AngularJS Input Radio](https://www.w3schools.com/angular/ng_ng-model.asp)

onelinerhub: [How do I use AngularJS to create a radio button?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-create-a-radio-button)