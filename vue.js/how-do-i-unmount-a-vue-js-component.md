# How do I unmount a Vue.js component?
// plain

To unmount a Vue.js component, you can use the `destroy` method. This method will remove the component from the DOM, as well as any of its event listeners and watchers.

## Example


```javascript
// create a new Vue instance
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

// unmount the component
app.$destroy()
```

The `destroy` method will not remove any data associated with the component, so you will need to manually clean up any data that was associated with the component.

The following list provides a breakdown of each part of the code:

1. `var app = new Vue({ ... })`: This line creates a new Vue instance and stores it in the `app` variable.
2. `el: '#app'`: This line tells the Vue instance to mount itself to the element with the ID of `app`.
3. `data: { message: 'Hello Vue!' }`: This line adds a `message` property to the Vue instance's `data` object.
4. `app.$destroy()`: This line calls the `destroy` method on the Vue instance, which will remove the component from the DOM.

For more information, please see the [Vue.js documentation on the `destroy` method](https://vuejs.org/v2/api/#vm-destroy).

onelinerhub: [How do I unmount a Vue.js component?](https://onelinerhub.com/vue.js/how-do-i-unmount-a-vue-js-component)