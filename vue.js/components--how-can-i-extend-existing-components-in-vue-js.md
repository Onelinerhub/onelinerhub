# components

How can I extend existing components in Vue.js?
// plain

Vue.js components are modular and reusable pieces of code that can be used to extend existing components. To extend an existing component, you can use the `extend` option in the `Vue.component` function. This option allows you to create a new component by extending an existing one.

For example, to extend the `my-button` component, you can use the following code:

```
Vue.component('my-extended-button', {
  extend: 'my-button',
  data () {
    return {
      text: 'Extended Button'
    }
  }
})
```

This will create a new component `my-extended-button` that is based on the `my-button` component. The new component will have the same properties and methods as the original component, but with the additional `text` property. The output of this code will be a new component with the `text` property set to `Extended Button`.

The `extend` option also allows you to add additional methods and computed properties to the extended component. For example, you can add a new method `sayHello` to the `my-extended-button` component as follows:

```
Vue.component('my-extended-button', {
  extend: 'my-button',
  data () {
    return {
      text: 'Extended Button'
    }
  },
  methods: {
    sayHello () {
      console.log('Hello!')
    }
  }
})
```

This will add the `sayHello` method to the `my-extended-button` component. When the method is called, it will output `Hello!` to the console.

Extending existing components is a powerful way to create custom components in Vue.js. It allows you to easily reuse existing components and add additional functionality to them.

## Helpful links

- [Vue.js Component API](https://vuejs.org/v2/api/#Vue-component)
- [Vue.js extend API](https://vuejs.org/v2/api/#Vue-extend)

onelinerhub: [components

How can I extend existing components in Vue.js?](https://onelinerhub.com/vue.js/components--how-can-i-extend-existing-components-in-vue-js)