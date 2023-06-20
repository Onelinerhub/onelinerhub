# How do I use a Vue.js CDN?
// plain

Using a Vue.js CDN (Content Delivery Network) is a great way to quickly get up and running with Vue.js.

To use a Vue.js CDN, you will need to include a `<script>` tag in your HTML page, pointing to the CDN URL for the version of Vue.js you want to use. For example:

```
<script src="https://cdn.jsdelivr.net/npm/vue@2.5.17/dist/vue.js"></script>
```

This will include the Vue.js library in your page, allowing you to use it in your JavaScript code.

You can also include other libraries from the Vue.js CDN, such as Vuex and Vue Router. For example:

```
<script src="https://cdn.jsdelivr.net/npm/vue@2.5.17/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuex@3.1.1/dist/vuex.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue-router@3.0.1/dist/vue-router.js"></script>
```

Once you have included the Vue.js library in your page, you can use it in your JavaScript code. For example:

```
const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

This example will create a new Vue instance, which will be associated with the HTML element with the `id` of `app`.

## Helpful links
- [Vue.js CDN](https://vuejs.org/v2/guide/installation.html#CDN)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How do I use a Vue.js CDN?](https://onelinerhub.com/vue.js/how-do-i-use-a-vue-js-cdn)