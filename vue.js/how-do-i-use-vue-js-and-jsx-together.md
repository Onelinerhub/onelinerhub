# How do I use Vue.js and JSX together?
// plain

Vue.js and JSX can be used together to create powerful user interfaces. In order to use them together, you need to install the `vue-jsx` plugin and `babel-plugin-transform-vue-jsx` to your project.

Here is an example of a Vue component using JSX:
```
<template>
  <div>
    <h1>Hello World!</h1>
    <MyComponent />
  </div>
</template>

<script>
import MyComponent from './MyComponent.vue'

export default {
  components: {
    MyComponent
  }
}
</script>
```

This example uses the `template` tag to define the HTML markup of the component, and the `script` tag to define the JavaScript code. The `MyComponent` component is imported from the `MyComponent.vue` file and registered as a component.

The `vue-jsx` plugin allows you to write JSX within the `template` tag, like this:
```
<template>
  <div>
    <h1>Hello World!</h1>
    <MyComponent>
      <h2>Hello from JSX!</h2>
    </MyComponent>
  </div>
</template>
```

The `babel-plugin-transform-vue-jsx` plugin allows you to write JSX within the `script` tag, like this:
```
<script>
import MyComponent from './MyComponent.vue'

export default {
  components: {
    MyComponent
  },
  render() {
    return (
      <div>
        <h1>Hello World!</h1>
        <MyComponent>
          <h2>Hello from JSX!</h2>
        </MyComponent>
      </div>
    )
  }
}
</script>
```

This example uses the `render` function to return the JSX markup, which is then rendered by the Vue component.

## Code explanation
**
- `<template>` tag: defines the HTML markup of the component
- `<script>` tag: defines the JavaScript code
- `import MyComponent from './MyComponent.vue'`: imports the `MyComponent` component from the `MyComponent.vue` file
- `components: { MyComponent }`: registers the `MyComponent` component
- `<MyComponent>`: renders the `MyComponent` component
- `render()` function: returns the JSX markup, which is then rendered by the Vue component

**## Helpful links**
- [Vue.js and JSX](https://vuejs.org/v2/guide/render-function.html#JSX)
- [vue-jsx plugin](https://github.com/vuejs/babel-plugin-transform-vue-jsx)
- [babel-plugin-transform-vue-jsx plugin](https://github.com/vuejs/babel-plugin-transform-vue-jsx)

onelinerhub: [How do I use Vue.js and JSX together?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-and-jsx-together)