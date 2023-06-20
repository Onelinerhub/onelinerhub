# How do I use Vue.js lifecycle hooks?
// plain

Vue.js lifecycle hooks are a powerful tool for managing the different stages of a component's life cycle. They allow developers to run code at specific points in the life cycle, such as before a component is created, before it is destroyed, or when it is updated.

Below is an example of using the `created` hook, which is run when a component is created:

```
// Inside the Vue component
created() {
  console.log('Component created!');
}
```

## Output example
 `Component created!`

The code above will log the string `Component created!` to the console when the component is created.

The following are the different Vue.js lifecycle hooks available:

- `beforeCreate`: Runs before the instance is initialized
- `created`: Runs after the instance is initialized
- `beforeMount`: Runs before the component is mounted to the DOM
- `mounted`: Runs after the component is mounted to the DOM
- `beforeUpdate`: Runs before data changes cause the component to re-render
- `updated`: Runs after the component is updated
- `beforeDestroy`: Runs before the instance is destroyed
- `destroyed`: Runs after the instance is destroyed

For more information, see the [Vue.js documentation](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram).

onelinerhub: [How do I use Vue.js lifecycle hooks?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-lifecycle-hooks)