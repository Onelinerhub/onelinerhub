# How do I use Quasar with Vue.js?
// plain

Quasar is a framework built on top of Vue.js that provides a set of tools and components to help developers build high-performance, responsive, and feature-rich applications. To use Quasar with Vue.js, you need to install the Quasar CLI and create a new project.

The following example shows how to install the Quasar CLI and create a new project:

```
$ npm install -g @quasar/cli
$ quasar create my-project
```

The `quasar create` command will create a new project in the `my-project` directory and install all the necessary dependencies. After the installation is complete, you can start the development server with the `quasar dev` command.

Once the development server is running, you can start building your application with Quasar and Vue.js. To do this, you need to create a new Vue component in the `src/components` directory and then add it to the `src/router.js` file.

The following example shows how to create a new component and add it to the router:

```js
// src/components/MyComponent.vue
<template>
  <h1>My Component</h1>
</template>

// src/router.js
import MyComponent from './components/MyComponent.vue'

export default new Router({
  routes: [
    {
      path: '/my-component',
      name: 'MyComponent',
      component: MyComponent
    }
  ]
})
```

Once the component is added to the router, you can access it at `/my-component` in the browser.

To learn more about using Quasar with Vue.js, you can check out the [Quasar documentation](https://quasar.dev/start/introduction).

## Helpful links

- [Quasar Documentation](https://quasar.dev/start/introduction)

onelinerhub: [How do I use Quasar with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-quasar-with-vue-js)