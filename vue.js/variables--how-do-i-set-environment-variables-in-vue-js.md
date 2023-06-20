# variables

How do I set environment variables in Vue.js?
// plain

Setting environment variables in Vue.js is a great way to store configuration values for your app. It allows you to easily access and edit these values without having to change the code.

To set environment variables in Vue.js, you can use the `Vue.config.productionTip` and `Vue.config.devtools` properties.

For example:
```
Vue.config.productionTip = false;
Vue.config.devtools = true;
```

This code will set the `productionTip` to false, and the `devtools` to true.

## Code explanation


- `Vue.config.productionTip`: This property sets whether to display a production tip on the console when Vue is running in production mode.
- `Vue.config.devtools`: This property sets whether to enable the Vue Devtools browser extension.

Here are some relevant links if you need more information:

- [Vue.js Environment Variables](https://vuejs.org/v2/guide/environment-variables.html)
- [Vue.config](https://vuejs.org/v2/api/#Vue-config)

onelinerhub: [variables

How do I set environment variables in Vue.js?](https://onelinerhub.com/vue.js/variables--how-do-i-set-environment-variables-in-vue-js)