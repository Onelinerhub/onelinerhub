# How do I use the md-datepicker component in AngularJS?
// plain

The `md-datepicker` component in AngularJS can be used to easily create a date picker for date input fields.

To use it, you first need to include the `angular-material` library in your HTML file.

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-animate.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-aria.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.5/angular-messages.min.js"></script>

<script src="https://ajax.googleapis.com/ajax/libs/angular_material/1.1.0/angular-material.min.js"></script>
```

Then you need to add the `md-datepicker` directive to your HTML file.

```html
<md-datepicker ng-model="myDate"></md-datepicker>
```

You can also set the date format and min/max date using the `md-date-format` and `md-min-date`/`md-max-date` attributes.

```html
<md-datepicker ng-model="myDate" md-date-format="dd/MM/yyyy" md-min-date="minDate" md-max-date="maxDate"></md-datepicker>
```

You can also customize the look and feel of the date picker using the `md-theme` attribute.

```html
<md-datepicker ng-model="myDate" md-theme="myTheme"></md-datepicker>
```

For more information, please refer to the [Angular Material documentation](https://material.angularjs.org/latest/demo/datepicker).

onelinerhub: [How do I use the md-datepicker component in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-md-datepicker-component-in-angularjs)