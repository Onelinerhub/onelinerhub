# How do I use the onChanges feature of AngularJS?
// plain

The `onChanges` feature of AngularJS allows you to watch for changes in an object and respond to them. It is typically used to detect and respond to changes in a component's input properties.

Here is an example of using `onChanges`:
```javascript
@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnChanges {
  @Input() name: string;

  ngOnChanges(changes: SimpleChanges) {
    if (changes.name) {
      console.log(`Name changed to ${changes.name.currentValue}`);
    }
  }
}
```

In this example, the `onChanges` feature is used to detect changes in the `name` input property. When the `name` property is changed, the `ngOnChanges` function will be called, and the new value of the `name` property will be logged to the console.

## Code explanation


1. `@Component`: This is a decorator used to define the component.
2. `@Input() name: string`: This is an input property of the component.
3. `ngOnChanges(changes: SimpleChanges)`: This is a function that is called when an input property is changed.
4. `if (changes.name)`: This checks if the `name` input property has changed.
5. `console.log(`Name changed to ${changes.name.currentValue}`)`: This logs the new value of the `name` property to the console.

Here are some ## Helpful links

- [Angular Documentation - OnChanges](https://angular.io/api/core/OnChanges)
- [Angular Tutorial - OnChanges](https://angular.io/tutorial/toh-pt5#onchanges)

onelinerhub: [How do I use the onChanges feature of AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-the-onchanges-feature-of-angularjs)