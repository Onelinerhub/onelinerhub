# How do I create a popover using AngularJS?
// plain

Creating a popover using AngularJS requires the use of the [Angular UI Bootstrap library](https://angular-ui.github.io/bootstrap/). This library provides a directive called `uib-popover` that can be used to create a popover.

Here is an example of how to use the `uib-popover` directive:

```
<button type="button" uib-popover="Popover Text" popover-title="Popover Title">Popover Button</button>
```

When the button is clicked, the popover will appear with the title "Popover Title" and the text "Popover Text".

The `uib-popover` directive has several parameters that can be used to customize the popover. These parameters include `popover-title`, `popover-trigger`, `popover-placement`, and `popover-append-to-body`.

For example, the `popover-trigger` parameter specifies the event that will trigger the popover. The following code snippet sets the trigger to `mouseenter`:

```
<button type="button" uib-popover="Popover Text" popover-title="Popover Title" popover-trigger="mouseenter">Popover Button</button>
```

Now when the mouse cursor enters the button, the popover will appear.

For more information on using the `uib-popover` directive, please refer to the [Angular UI Bootstrap Popover documentation](https://github.com/angular-ui/bootstrap/tree/master/src/popover).

onelinerhub: [How do I create a popover using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-a-popover-using-angularjs)