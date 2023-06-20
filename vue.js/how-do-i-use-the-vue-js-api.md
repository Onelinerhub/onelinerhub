# How do I use the Vue.js API?
// plain

Using the Vue.js API is a simple process.

First, you must include the Vue.js library in your HTML file.

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

Then, you can create a new Vue instance with the `new Vue()` command. This instance will contain all of the configuration options for your Vue application.

```
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World'
  }
})
```

You can then use the `{{ }}` syntax to access the data from the Vue instance in your HTML.

```
<div id="app">
  {{ message }}
</div>
```

The output of this code will be `Hello World`.

You can also use the Vue instance to add methods and lifecycle hooks to your application.

```
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

The `reverseMessage` method can then be called from the HTML.

```
<div id="app">
  {{ message }}
  <button @click="reverseMessage">Reverse Message</button>
</div>
```

Clicking the button will reverse the message, so the output of the code will be `dlroW olleH`.

## Helpful links

- [Vue.js Official Documentation](https://vuejs.org/v2/guide/)
- [Vue.js API Reference](https://vuejs.org/v2/api/)

onelinerhub: [How do I use the Vue.js API?](https://onelinerhub.com/vue.js/how-do-i-use-the-vue-js-api)