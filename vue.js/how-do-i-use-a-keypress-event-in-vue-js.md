# How do I use a keypress event in Vue.js?
// plain

Using a keypress event in Vue.js is simple and easy. To do so, you must first create a method that will be called when a keypress event occurs.

For example, a method called `handleKeyPress` can be created as follows:
```javascript
methods: {
  handleKeyPress(event) {
    // handle keypress event
  }
}
```

Then, the `v-on` directive can be used to bind the `keypress` event to the method.

```html
<input v-on:keypress="handleKeyPress" />
```

The `event` argument passed to the method contains the keycode of the key pressed. This can be used to determine which key was pressed.

```javascript
methods: {
  handleKeyPress(event) {
    if (event.keyCode === 13) {
      console.log('Enter key was pressed');
    }
  }
}
```

The output of the above code would be:
```
Enter key was pressed
```

For more information, refer to the [Vue.js documentation](https://vuejs.org/v2/guide/events.html#Key-Modifiers).

## Code explanation
**
- `methods: { ... }`: This is the object where the method is defined.
- `handleKeyPress(event) { ... }`: This is the method that is called when a keypress event occurs. The `event` argument passed to the method contains the keycode of the key pressed.
- `<input v-on:keypress="handleKeyPress" />`: This is the HTML element which binds the `keypress` event to the method.
- `if (event.keyCode === 13) { ... }`: This is the condition that checks if the `Enter` key was pressed. If it was, the message `Enter key was pressed` is logged in the console.

**## Helpful links**
- [Vue.js documentation](https://vuejs.org/v2/guide/events.html#Key-Modifiers)

onelinerhub: [How do I use a keypress event in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-a-keypress-event-in-vue-js)