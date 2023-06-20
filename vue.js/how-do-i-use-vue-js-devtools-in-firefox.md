# How do I use Vue.js devtools in Firefox?
// plain

The Vue.js devtools are a browser extension that can be used to debug and inspect Vue.js applications. To use the devtools in Firefox, you must first install the [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/) addon from the Firefox Add-ons store.

Once installed, you can open the devtools in Firefox by pressing **Ctrl** + **Shift** + **I** or by selecting the **Vue** tab in the Firefox Developer Tools.

The devtools will then appear in the bottom of the browser window. From here you can inspect the components and data of your Vue.js application.

For example, if you have a component with data like this:

```
<template>
  <div>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: 'Hello World',
      message: 'This is a message from Vue.js'
    }
  }
}
</script>
```

You can inspect the component's data in the devtools:

![Vue.js devtools screenshot](https://i.imgur.com/UjX6Jvz.png)

The devtools also allow you to edit the data and see the changes in real-time.

For more information on using the Vue.js devtools, see the [Vue.js devtools documentation](https://vue-devtools.github.io/docs/).

onelinerhub: [How do I use Vue.js devtools in Firefox?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-devtools-in-firefox)