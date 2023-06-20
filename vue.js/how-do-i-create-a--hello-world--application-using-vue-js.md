# How do I create a "Hello World" application using Vue.js?
// plain

Creating a "Hello World" application using Vue.js is quite easy. Here is an example of the code you need to write:

```
<div id="app">
  {{ message }}
</div>

<script>
  new Vue({
    el: '#app',
    data: {
      message: 'Hello World!'
    }
  })
</script>
```

The output of this code will be:

```
Hello World!
```

This code consists of the following parts:

1. **The HTML template**: This is the `<div>` element with the `id="app"` attribute, inside which the `{{ message }}` expression is placed. This expression is used to output the value of the `message` data property.

2. **The Vue instance**: This is the `new Vue()` constructor function, which is used to create a new Vue instance. This instance is bound to the `#app` element and has a `data` property, which contains the `message` property with the value `"Hello World!"`.

For more information on how to use Vue.js, please refer to the [Vue.js documentation](https://vuejs.org/v2/guide/).

onelinerhub: [How do I create a "Hello World" application using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-create-a--hello-world--application-using-vue-js)