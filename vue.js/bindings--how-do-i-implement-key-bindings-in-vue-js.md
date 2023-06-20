# bindings

How do I implement key bindings in Vue.js?
// plain

Key bindings in Vue.js are implemented using the `v-on` directive. This directive binds a DOM event to a method in the component. For example, the following code binds the `keyup` event to a method called `onKeyup`:

```
<input v-on:keyup="onKeyup" />
```

The `onKeyup` method can then be defined in the component's methods section, like this:

```
methods: {
  onKeyup(event) {
    console.log(event.key);
  }
}
```

This code will log the pressed key to the console.

## Code explanation


- `v-on` directive - binds a DOM event to a method in the component
- `keyup` event - the DOM event to be bound
- `onKeyup` method - the method in the component to be called when the event is triggered
- `event` object - the event object passed to the method
- `event.key` - the pressed key value

## Helpful links

- [Vue.js Documentation - Handling User Input](https://vuejs.org/v2/guide/events.html#Handling-User-Input)
- [Vue.js Documentation - Event Handling](https://vuejs.org/v2/guide/events.html)

onelinerhub: [bindings

How do I implement key bindings in Vue.js?](https://onelinerhub.com/vue.js/bindings--how-do-i-implement-key-bindings-in-vue-js)