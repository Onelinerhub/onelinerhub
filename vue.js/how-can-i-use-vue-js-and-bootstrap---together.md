# How can I use Vue.js and Bootstrap 5 together?
// plain

Vue.js and Bootstrap 5 can be used together to create dynamic web applications. To do this, you will need to install both the Vue.js and Bootstrap 5 packages.

Once the packages are installed, you can use the Bootstrap 5 components within your Vue.js application. For example:

```
<template>
  <div>
    <b-button variant="primary">Primary</b-button>
  </div>
</template>

<script>
  import { BButton } from 'bootstrap-vue'

  export default {
    components: {
      BButton
    }
  }
</script>
```

This will render a Bootstrap 5 primary button on the page.

## Code explanation


1. `<template>` - This is the HTML markup that will be rendered on the page.
2. `<script>` - This is the Vue.js code that will be executed when the component is loaded.
3. `import { BButton } from 'bootstrap-vue'` - This is the line that imports the Bootstrap 5 button component from the Bootstrap Vue package.
4. `components: { BButton }` - This is the line that registers the Bootstrap 5 button component with the Vue.js application.

For more information, please see the following links:

- [Vue.js Documentation](https://vuejs.org/v2/guide/)
- [Bootstrap Vue Documentation](https://bootstrap-vue.org/docs)

onelinerhub: [How can I use Vue.js and Bootstrap 5 together?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-and-bootstrap---together)