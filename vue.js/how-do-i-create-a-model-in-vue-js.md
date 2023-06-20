# How do I create a model in Vue.js?
// plain

Creating a model in Vue.js is very straightforward. To start, you need to create a new Vue instance and give it a data object. This data object will contain the properties that will become the model. For example:

```
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World'
  }
})
```

The above code creates a Vue instance and adds a `message` property to the model. This property can be accessed from the template using the `{{ message }}` syntax.

To add more properties to the model, simply add them to the `data` object. For example:

```
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World',
    count: 0
  }
})
```

The `count` property can be accessed from the template using the `{{ count }}` syntax.

To update the model, you can use the `Vue.set()` method. For example:

```
Vue.set(app.data, 'name', 'John Doe');
```

This code adds a `name` property to the model and sets it to `John Doe`.

You can also use the `Vue.delete()` method to remove properties from the model. For example:

```
Vue.delete(app.data, 'name');
```

This code removes the `name` property from the model.

## Helpful links
- [Vue.js Documentation](https://vuejs.org/v2/guide/)
- [Vue.set() API Reference](https://vuejs.org/v2/api/#Vue-set)
- [Vue.delete() API Reference](https://vuejs.org/v2/api/#Vue-delete)

onelinerhub: [How do I create a model in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-create-a-model-in-vue-js)