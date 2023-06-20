# How do I use Vue.js to hide an element?
// plain

To hide an element using Vue.js, you can use the `v-show` directive. This directive will conditionally render an element depending on the value of a boolean expression. For example:

```
<div id="app">
    <p v-show="showElement">This element will be hidden</p>
</div>

<script>
    new Vue({
        el: '#app',
        data: {
            showElement: false
        }
    })
</script>
```

In this example, the `<p>` element will not be rendered in the DOM since the value of `showElement` is `false`.

The parts of the code are as follows:

- `<div id="app">`: This is the root element of the Vue instance.
- `<p v-show="showElement">`: This is the element that will be conditionally rendered depending on the value of `showElement`.
- `new Vue({ ... })`: This is the Vue instance that is responsible for managing the data and rendering the DOM.
- `el: '#app'`: This tells the Vue instance which element to mount onto.
- `data: { showElement: false }`: This is the data that will be used to determine whether the element should be rendered or not.

For more information, see the [Vue.js documentation on v-show](https://vuejs.org/v2/api/#v-show).

onelinerhub: [How do I use Vue.js to hide an element?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-to-hide-an-element)