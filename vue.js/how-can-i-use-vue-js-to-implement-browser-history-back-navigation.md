# How can I use Vue.js to implement browser history back navigation?
// plain

Vue.js provides the `router` library that can be used to implement browser history back navigation. The `router` library provides the `beforeEach` navigation guard which can be used to detect navigation changes. The `beforeEach` navigation guard can be used to detect navigation changes and then programmatically call the `router.go()` method to navigate back in the browser history.

For example:
```js
router.beforeEach((to, from, next) => {
  if (to.path === '/back') {
    router.go(-1);
  }
  next();
});
```
This code will navigate back in the browser history when the `/back` route is visited.

Parts of the code:

- `router`: The Vue.js router library
- `beforeEach`: Navigation guard that is called before every navigation change
- `to.path`: Path of the route that is being navigated to
- `router.go(-1)`: Method to programmatically navigate back in the browser history

## Helpful links

- [Vue.js Router Documentation](https://router.vuejs.org/guide/)
- [Vue.js Router API Reference](https://router.vuejs.org/api/)

onelinerhub: [How can I use Vue.js to implement browser history back navigation?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-implement-browser-history-back-navigation)