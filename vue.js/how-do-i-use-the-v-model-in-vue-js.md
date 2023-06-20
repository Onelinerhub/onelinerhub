# How do I use the v-model in Vue.js?
// plain

The `v-model` directive is used in Vue.js to create two-way data bindings on form input, textarea, and select elements. It automatically picks up the value of the data model and updates it when the user changes the input.

```
<!-- example of v-model usage -->
<input type="text" v-model="message">

<script>
  new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue.js!'
    }
  });
</script>
```

The `v-model` directive binds the `message` data property to the `<input>` element. Any changes made to the `<input>` element will be reflected in the data model, and any changes made to the data model will be reflected in the `<input>` element.

## Code explanation


1. `v-model` - This is the directive that binds the data model to the element.
2. `message` - This is the data model that is being bound to the element.
3. `<input>` - This is the HTML element that the data model is being bound to.

For more information on using the `v-model` directive, check out the [Vue.js documentation](https://vuejs.org/v2/guide/forms.html).

onelinerhub: [How do I use the v-model in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-v-model-in-vue-js)