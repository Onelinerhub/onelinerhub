# event

How do I add a click event to a href element in Vue.js?
// plain

Adding a click event to a `<a>` element in Vue.js can be done with the `@click` directive. This directive allows you to add a click event listener to the element.

For example, given the following `<a>` element:

```
<a href="#" @click="handleClick">Click me</a>
```

You can add a click event listener to the element by defining a `handleClick` method in your Vue component:

```
methods: {
  handleClick() {
    alert('You clicked the link!');
  }
}
```

When the link is clicked, the `handleClick` method will be called, displaying an alert.

The `@click` directive can also accept an argument:

```
<a href="#" @click="handleClick('foo')">Click me</a>
```

The argument `foo` will be passed to the `handleClick` method:

```
methods: {
  handleClick(arg) {
    alert(`You clicked the link with argument ${arg}!`);
  }
}
```

When the link is clicked, the `handleClick` method will be called with the argument `foo`, displaying an alert.

#### Summary

- The `@click` directive can be used to add a click event listener to an `<a>` element in Vue.js.
- The `@click` directive can accept an argument, which will be passed to the event listener.

#### Links

- [Vue.js - Event Handling](https://vuejs.org/v2/guide/events.html)

onelinerhub: [event

How do I add a click event to a href element in Vue.js?](https://onelinerhub.com/vue.js/event--how-do-i-add-a-click-event-to-a-href-element-in-vue-js)