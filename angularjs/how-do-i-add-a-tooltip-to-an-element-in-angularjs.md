# How do I add a tooltip to an element in AngularJS?
// plain

To add a tooltip to an element in AngularJS, you can use the [Angular UI Bootstrap](https://angular-ui.github.io/bootstrap/) library. The library provides a [tooltip directive](https://angular-ui.github.io/bootstrap/#/tooltip) which can be used to add a tooltip to any element.

## Example code

```html
<div>
  <span uib-tooltip="This is a tooltip">Hover me</span>
</div>
```

The code above will add a tooltip to the `span` element which will be visible when the user hovers over the element.

The `uib-tooltip` directive takes a string as its value, which is the text to display in the tooltip.

The tooltip directive also supports a number of other options such as `tooltip-placement`, `tooltip-trigger`, `tooltip-append-to-body`, etc. which can be used to customize the tooltip.

## Helpful links
- [Angular UI Bootstrap](https://angular-ui.github.io/bootstrap/)
- [Tooltip Directive](https://angular-ui.github.io/bootstrap/#/tooltip)

onelinerhub: [How do I add a tooltip to an element in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-add-a-tooltip-to-an-element-in-angularjs)