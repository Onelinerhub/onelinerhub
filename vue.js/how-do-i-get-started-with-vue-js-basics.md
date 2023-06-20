# How do I get started with Vue.js basics?
// plain

Getting started with Vue.js basics is fairly easy. Here's an example of how to create a simple Vue instance:

```
<div id="app">
  {{ message }}
</div>

<script>
  // Create a Vue instance
  var app = new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  })
</script>
```
This example will output the message `Hello Vue!` in the `<div>` with the `id` of `app`.

The code consists of two parts:

1. The HTML: This defines the structure of the page and includes a `<div>` with the `id` of `app` and a `{{ message }}` variable.

2. The JavaScript: This defines the Vue instance and includes an `el` property that specifies the `<div>` where the instance will be mounted, and a `data` property that contains the `message` variable.

For more information about getting started with Vue.js, please refer to the [Vue.js documentation](https://vuejs.org/v2/guide/).

onelinerhub: [How do I get started with Vue.js basics?](https://onelinerhub.com/vue.js/how-do-i-get-started-with-vue-js-basics)