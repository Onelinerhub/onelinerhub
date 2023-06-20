# statement

How do I use an if statement with Vue.js?
// plain

An if statement is a way to check if a condition is true or false, and execute code based on the result. In Vue.js, you can use an if statement to conditionally render a section of your template. For example, if you wanted to show a message if a user has an account:

```
<template>
  <div>
    <h1>Welcome!</h1>
    <p v-if="userHasAccount">You have an account!</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userHasAccount: true
    }
  }
}
</script>
```

This will result in the following output:

```
<div>
  <h1>Welcome!</h1>
  <p>You have an account!</p>
</div>
```

## Code explanation


- `<template>`: This is the HTML template for the component.
- `<div>`: This is a container element that wraps the other elements in the template.
- `<h1>`: This is a heading element.
- `<p>`: This is a paragraph element.
- `v-if="userHasAccount"`: This is a Vue directive that tells Vue to conditionally render the element based on the value of the `userHasAccount` data property.
- `export default { }`: This is the Vue component object.
- `data() { }`: This is a method that returns the data properties of the component.
- `userHasAccount: true`: This is the data property that determines if the `<p>` element will be rendered or not.

For more information, see the [Vue.js documentation on conditionals](https://vuejs.org/v2/guide/conditional.html).

onelinerhub: [statement

How do I use an if statement with Vue.js?](https://onelinerhub.com/vue.js/statement--how-do-i-use-an-if-statement-with-vue-js)