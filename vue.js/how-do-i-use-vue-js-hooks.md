# How do I use Vue.js hooks?
// plain

Vue.js hooks are a way to use Vue features without having to write a component. They are functions that allow you to add functionality to existing components and to create custom components.

Here is an example of using a hook to create a custom component:

```
// MyComponent.vue
<template>
  <div>
    <h1>My Component</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import { useState } from 'vue'

export default {
  setup() {
    const [message, setMessage] = useState('Hello World!')
    return {
      message,
      setMessage
    }
  }
}
</script>
```

In this example, the `useState` hook is used to create a custom component called `MyComponent`. This component has a `message` property, which is set to `Hello World!` and a `setMessage` method which can be used to update the `message` property.

The list of available hooks can be found in the [Vue documentation](https://vuejs.org/v2/api/#Options-Data).

## Helpful links

- [Vue Documentation](https://vuejs.org/v2/api/#Options-Data)

onelinerhub: [How do I use Vue.js hooks?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-hooks)