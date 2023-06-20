# How can I use Vue.js mixins to create a reusable component?
// plain

Mixins in Vue.js are a great way to create a reusable component. Mixins allow you to extend existing components by adding custom methods and properties to them. This allows you to create a component that can be reused in multiple places without having to rewrite the code.

For example, the following code block creates a mixin that defines a `sayHello` method:
```
const SayHelloMixin = {
  methods: {
    sayHello() {
      console.log('Hello!')
    }
  }
}
```

When the `sayHello` method is called, the output would be:
```
Hello!
```

To use the mixin, we can add it to a component's `mixins` option:

```
Vue.component('my-component', {
  mixins: [SayHelloMixin]
})
```

The mixin is now available to the component. We can call the `sayHello` method as if it were part of the component itself:

```
this.$options.mixins[0].sayHello()
```

The output would be:
```
Hello!
```

Mixins are a great way to create reusable components in Vue.js. They are easy to use and can help you save time by not having to rewrite code.

## Helpful links
- [Vue.js Mixins](https://vuejs.org/v2/guide/mixins.html)
- [Vue.js Component Options](https://vuejs.org/v2/api/#Options-Data)

onelinerhub: [How can I use Vue.js mixins to create a reusable component?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-mixins-to-create-a-reusable-component)