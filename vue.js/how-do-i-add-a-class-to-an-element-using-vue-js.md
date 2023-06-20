# How do I add a class to an element using Vue.js?
// plain

To add a class to an element using Vue.js, you can use the `v-bind` directive. The `v-bind` directive can be used to dynamically bind one or more attributes, or a component prop, to an expression.

For example, to add a class `example-class` to an element:

```
<div v-bind:class="example-class">
  This div will have the class "example-class".
</div>
```

The code above includes the following parts:
- `v-bind:class` - The `v-bind` directive, used to bind an attribute to an expression
- `example-class` - The expression that is bound to the class attribute, in this case the class name

## Helpful links
- [Vue.js documentation - Class and Style Bindings](https://vuejs.org/v2/guide/class-and-style.html)
- [Vue.js documentation - The v-bind Directive](https://vuejs.org/v2/api/#v-bind)

onelinerhub: [How do I add a class to an element using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-add-a-class-to-an-element-using-vue-js)