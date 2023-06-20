# How do I get started with Vue.js?
// plain

Getting started with Vue.js is easy and straightforward.

1. First, include the Vue library in your HTML page.
```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

2. Create a Vue instance with a `data` object and a `template` string.
```
<div id="app">
  <p>{{ message }}</p>
</div>

<script>
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
</script>
```

3. Mount the Vue instance to the `#app` element.
```
app.$mount('#app')
```

4. Output:
```
<div id="app">
  <p>Hello Vue!</p>
</div>
```

You can find more information on how to get started with Vue.js in the official [Vue.js documentation](https://vuejs.org/v2/guide/).

onelinerhub: [How do I get started with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-get-started-with-vue-js)