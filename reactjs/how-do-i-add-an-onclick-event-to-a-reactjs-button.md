# How do I add an onclick event to a ReactJS button?
// plain

Adding an onclick event to a ReactJS button is a simple process. First, you need to create a function that will be called when the button is clicked. For example:

```
const myFunction = () => {
  console.log('Button clicked!');
}
```

Next, you need to add the onClick attribute to the button element and pass in the function as the value.

```
<button onClick={myFunction}>Click Me!</button>
```

When the button is clicked, the `myFunction` function will be called and the message `Button clicked!` will be logged to the console.

## Code explanation

- `const myFunction = () => {` - This is the start of the function that will be called when the button is clicked
- `console.log('Button clicked!');` - This is the code that will be executed when the button is clicked
- `<button onClick={myFunction}>Click Me!</button>` - This is the button element with the onClick attribute set to the `myFunction` function

## Helpful links
- [React Documentation - Events](https://reactjs.org/docs/handling-events.html)
- [MDN - onClick Event](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick)

onelinerhub: [How do I add an onclick event to a ReactJS button?](https://onelinerhub.com/reactjs/how-do-i-add-an-onclick-event-to-a-reactjs-button)