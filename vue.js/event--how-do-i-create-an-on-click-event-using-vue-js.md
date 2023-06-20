# event

How do I create an on click event using Vue.js?
// plain

Creating an on click event using Vue.js is quite simple. First, you need to create a method in the Vue instance that will be triggered when the event is fired. You can do this by adding the method to the `methods` object in the Vue instance. For example:

```
new Vue({
  el: '#app',
  methods: {
    handleClick: function() {
      console.log('clicked!');
    }
  }
});
```

Then, you can bind the method to the element you want to listen to the click event on, using the `v-on` directive. For example:

```
<button v-on:click="handleClick">Click me</button>
```

When the button is clicked, the `handleClick` method will be triggered.

## Code explanation


- `new Vue`: This is where you create the Vue instance, and it is the root of your application.
- `el`: This is the element that your Vue instance will be attached to.
- `methods`: This is an object where you can define methods that can be used in the Vue instance.
- `handleClick`: This is the method that will be triggered when the click event is fired.
- `v-on`: This is the Vue directive used for event handling.
- `click`: This is the event that will be listened for.
- `handleClick`: This is the method that will be called when the click event is fired.

## Helpful links

- [Vue.js Event Handling Documentation](https://vuejs.org/v2/guide/events.html)
- [Vue.js Instance Documentation](https://vuejs.org/v2/guide/instance.html)

onelinerhub: [event

How do I create an on click event using Vue.js?](https://onelinerhub.com/vue.js/event--how-do-i-create-an-on-click-event-using-vue-js)