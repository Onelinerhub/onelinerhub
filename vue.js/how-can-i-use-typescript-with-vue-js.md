# How can I use TypeScript with Vue.js?
// plain

Using TypeScript with Vue.js is a great way to add type safety and object-oriented programming to your Vue.js projects. Here is an example of how to use TypeScript with Vue.js.

```js
// App.vue
<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  data() {
    return {
      message: 'Hello Vue and TypeScript!'
    }
  }
})
</script>
```

This example creates a new Vue component that displays a message using the data property.

The `<script>` tag has a `lang` attribute set to `ts` to indicate that TypeScript is being used. The `Vue.extend()` function is used to create a new Vue component. The `data` property is used to store the message that will be displayed.

Here are some useful links for further information:
- [Vue.js and TypeScript guide](https://vuejs.org/v2/guide/typescript.html)
- [Vue CLI TypeScript guide](https://cli.vuejs.org/guide/typescript.html)
- [TypeScript and Vue.js tutorial](https://www.sitepoint.com/typescript-and-vue-js-getting-started/)

onelinerhub: [How can I use TypeScript with Vue.js?](https://onelinerhub.com/vue.js/how-can-i-use-typescript-with-vue-js)