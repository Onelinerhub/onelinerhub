# How do I install Vue.js?
// plain

Vue.js is a progressive JavaScript framework that can be used to create interactive web interfaces. It is designed to be incrementally adoptable, and can be integrated into existing projects or used to create new ones.

The easiest way to install Vue.js is to use a package manager like npm or yarn.

For example, to install Vue.js with npm, run the following command in the terminal:

```
$ npm install vue
```

This will install the latest version of Vue.js and all of its required dependencies.

Alternatively, you can also use the CDN to include the Vue.js library in your project:

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

Once Vue.js is installed, you can create a new Vue instance, and mount it to a DOM element:

```
const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World!'
  }
})
```

This will create a new Vue instance, and mount it to the DOM element with the ID of 'app'.

## Helpful links

- [Vue.js Installation Guide](https://vuejs.org/v2/guide/installation.html)
- [npm Documentation](https://docs.npmjs.com/)
- [yarn Documentation](https://yarnpkg.com/en/docs)

onelinerhub: [How do I install Vue.js?](https://onelinerhub.com/vue.js/how-do-i-install-vue-js)