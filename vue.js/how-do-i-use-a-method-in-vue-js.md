# How do I use a method in Vue.js?
// plain

Using a method in Vue.js is a straightforward process. To begin, you need to define the method in the `methods` object in the `Vue` instance:

```js
new Vue({
  data: {
    message: 'Hello world!'
  },
  methods: {
    greet: function() {
      alert(this.message);
    }
  }
});
```

Then, you can call the method from within the template using the `v-on` directive:

```html
<div>
  <button v-on:click="greet">Greet</button>
</div>
```

When the button is clicked, the `greet` method will be called, and an alert with the message `Hello world!` will be displayed.

## Code explanation


1. Define the method in the `methods` object in the `Vue` instance.
2. Use the `v-on` directive to call the method from within the template.

Relevant links for further reading:

- [Vue.js documentation - Methods](https://vuejs.org/v2/guide/methods.html)
- [Vue.js documentation - Events](https://vuejs.org/v2/guide/events.html)

onelinerhub: [How do I use a method in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-a-method-in-vue-js)