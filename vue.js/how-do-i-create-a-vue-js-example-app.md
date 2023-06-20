# How do I create a Vue.js example app?
// plain

1. To create a Vue.js example app, first install the Vue CLI (command line interface) by running `npm install -g @vue/cli` in your terminal.

2. Create a new project using the Vue CLI by running `vue create my-app` in your terminal, where `my-app` is the name of your app.

3. Once the project is created, you can navigate to the project directory and start the development server by running `cd my-app && npm run serve`.

4. Create a new component in the `src/components` folder and add the following code to it:
```
<template>
  <div>Hello World!</div>
</template>

<script>
export default {
  name: 'MyComponent'
}
</script>
```
5. Add the component to the `App.vue` file:
```
<template>
  <div>
    <MyComponent />
  </div>
</template>

<script>
import MyComponent from './components/MyComponent.vue'

export default {
  components: {
    MyComponent
  }
}
</script>
```
6. Now if you open `localhost:8080`, you should see the text "Hello World!" on the page.

7. To learn more about creating Vue.js apps, check out the [Vue.js documentation](https://vuejs.org/v2/guide/).

onelinerhub: [How do I create a Vue.js example app?](https://onelinerhub.com/vue.js/how-do-i-create-a-vue-js-example-app)