# rendering

How do I use Vue.js to render a list?
// plain

Vue.js is a popular JavaScript library for building user interfaces. To render a list with Vue.js, you need to create a Vue instance with a template containing a `v-for` directive. The `v-for` directive allows you to iterate over an array of data and render each item in the array.

For example, if you have an array of names stored in a variable called `names`, you can render a list of those names with the following code:

```html
<div id="app">
  <ul>
    <li v-for="name in names">{{ name }}</li>
  </ul>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      names: ['John', 'Paul', 'George', 'Ringo']
    }
  })
</script>
```

This code will render the following output:

```
John
Paul
George
Ringo
```

The `v-for` directive consists of three parts:

* `name` - The variable name that will be used to refer to each item in the array.
* `in` - The keyword that separates the variable name from the array.
* `names` - The array of data that will be iterated over.

For more information on using the `v-for` directive to render lists, see the [Vue.js documentation](https://vuejs.org/v2/guide/list.html).

onelinerhub: [rendering

How do I use Vue.js to render a list?](https://onelinerhub.com/vue.js/rendering--how-do-i-use-vue-js-to-render-a-list)