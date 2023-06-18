# event

How do I add an onclick event to a ReactJS component?
// plain

An onclick event can be added to a ReactJS component by using the `onClick` attribute. This attribute takes a function as its argument which will be called when the element is clicked. The following example code block shows how to add an onclick event to a ReactJS component:

```
<button onClick={() => alert('Button clicked!')}>
  Click Me
</button>
```

When the button is clicked, the alert `Button clicked!` will be displayed.

The code can be broken down into the following parts:

- `<button>`: This is the HTML element that will be clicked.
- `onClick`: This is the attribute that will trigger the event when the element is clicked.
- `() =>`: This is the arrow function that will be called when the element is clicked.
- `alert('Button clicked!')`: This is the JavaScript code that will be executed when the element is clicked.

## Helpful links

- [React Events](https://reactjs.org/docs/events.html)
- [Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

onelinerhub: [event

How do I add an onclick event to a ReactJS component?](https://onelinerhub.com/reactjs/event--how-do-i-add-an-onclick-event-to-a-reactjs-component)