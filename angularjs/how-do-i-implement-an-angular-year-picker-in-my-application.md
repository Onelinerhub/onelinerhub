# How do I implement an Angular year picker in my application?
// plain

This can be done by using an Angular UI library, such as PrimeNG or Angular Material, to create a year picker component. The following example code shows how to implement a year picker using the PrimeNG library:

```
<p-calendar [(ngModel)]="date" [showTime]="false" [monthNavigator]="true" [yearNavigator]="true" [yearRange]="yearRange"></p-calendar>

export class AppComponent {
  date: Date;
  yearRange: string;

  constructor() {
    this.yearRange = (new Date().getFullYear() - 100) + ':' + (new Date().getFullYear() + 100);
  }
}
```

The `<p-calendar>` component has several properties that can be used to configure the year picker. The `[monthNavigator]` and `[yearNavigator]` properties are set to `true` to enable the month and year picker. The `[yearRange]` property is set to a range of years to limit the selection of years the user can choose from. In this case, the range is set to 100 years before and after the current year.

## Code explanation


- `<p-calendar>`: This is the PrimeNG component used to create the year picker.
- `[monthNavigator]="true"`: This property is set to `true` to enable the month picker.
- `[yearNavigator]="true"`: This property is set to `true` to enable the year picker.
- `[yearRange]="yearRange"`: This property is set to the `yearRange` variable to limit the selection of years the user can choose from.
- `yearRange: string`: This is the variable used to store the range of years used by the `[yearRange]` property.
- `this.yearRange = (new Date().getFullYear() - 100) + ':' + (new Date().getFullYear() + 100)`: This is the line of code used to set the `yearRange` variable to a range of 100 years before and after the current year.

## Helpful links
- PrimeNG: https://www.primefaces.org/primeng/
- Angular Material: https://material.angular.io/

onelinerhub: [How do I implement an Angular year picker in my application?](https://onelinerhub.com/angularjs/how-do-i-implement-an-angular-year-picker-in-my-application)