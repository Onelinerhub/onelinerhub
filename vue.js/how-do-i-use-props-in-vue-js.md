# How do I use props in Vue.js?
// plain

Props are custom attributes you can register on a component that let you pass data from a parent component to a child component. In Vue.js, props are custom attributes you register on a component. They provide a way to pass data from the parent component to the child component.

Here is an example of how to use props in Vue.js:

```
// Parent component
<template>
  <ChildComponent message="Hello World!" />
</template>

// Child component
<template>
  <div>{{ message }}</div>
</template>

<script>
export default {
  props: {
    message: String
  }
}
</script>
```

The output of this example code would be:
```
Hello World!
```

## Code explanation

- The parent component contains a `<ChildComponent>` tag with a `message` attribute containing the string `Hello World!`.
- In the child component, the `message` prop is declared in the `props` section of the `export` statement.
- A `<div>` element is used to render the message prop.

## Helpful links
- [Vue.js Props Documentation](https://vuejs.org/v2/guide/components-props.html)
- [Vue.js Props Tutorial](https://michaelnthiessen.com/getting-started-with-vue-props/)

onelinerhub: [How do I use props in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-props-in-vue-js)