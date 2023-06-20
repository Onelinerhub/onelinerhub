# How do I keep my Vue.js application alive?
// plain

Keeping a Vue.js application alive is a two-step process:

1. Implementing a process manager: A process manager will keep the application running in the background, and will restart the application if it crashes. Popular process managers for Vue.js applications include PM2, Forever, and Upstart.

2. Implementing a lifecycle hook: A lifecycle hook will be triggered when the application is started, and can be used to perform any necessary tasks. For example, the `created` hook can be used to fetch data from an API and store it in the application's state.

```js
new Vue({
  el: '#app',
  created() {
    // Fetch data from API
    fetch('http://example.com/data')
      .then(response => response.json())
      .then(data => {
        // Store data in application's state
        this.$store.state.data = data;
      });
  }
});
```

## Helpful links
- [PM2](https://pm2.keymetrics.io/)
- [Forever](https://www.npmjs.com/package/forever)
- [Upstart](http://upstart.ubuntu.com/)
- [Vue.js Lifecycle Hooks](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)

onelinerhub: [How do I keep my Vue.js application alive?](https://onelinerhub.com/vue.js/how-do-i-keep-my-vue-js-application-alive)