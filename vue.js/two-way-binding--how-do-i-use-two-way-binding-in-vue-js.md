# two-way binding

How do I use two-way binding in Vue.js?
// plain

Two-way binding in Vue.js allows for the updating of a data property to be reflected in the view, and for changes in the view to be reflected in the data property. This is accomplished through the use of the `v-model` directive.

Here is an example of two-way binding in action:

```
<div id="app">
  <input type="text" v-model="message">
  <p>{{ message }}</p>
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      message: 'Hello World!'
    }
  });
</script>
```

This code will render an input field and a paragraph tag, both displaying the text "Hello World!", and any changes made to the input field will be reflected in the paragraph tag, and vice versa.

The `v-model` directive consists of the following parts:

- `v-model` - the directive itself, which binds the data property to the view
- `message` - the data property that is being bound
- `input type="text"` - the view element that is being bound

For further information on two-way binding in Vue.js, see the following links:

- [Vue.js documentation on two-way binding](https://vuejs.org/v2/guide/forms.html#Two-Way-Binding)
- [Vue Mastery tutorial on two-way binding](https://www.vuemastery.com/courses/intro-to-vue-js/v-model/)

onelinerhub: [two-way binding

How do I use two-way binding in Vue.js?](https://onelinerhub.com/vue.js/two-way-binding--how-do-i-use-two-way-binding-in-vue-js)