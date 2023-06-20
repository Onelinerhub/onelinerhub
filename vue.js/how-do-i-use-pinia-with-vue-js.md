# How do I use Pinia with Vue.js?
// plain

Pinia is a library that provides a set of utilities to help you manage state in Vue.js applications. It is designed to work with the Composition API and provides a set of APIs to make state management easier.

To use Pinia with Vue.js, you first need to install the library:

```
npm install pinia
```

Once installed, you can use the `usePinia` hook in your components to access the Pinia store and its APIs.

```js
import { usePinia } from 'pinia'

export default {
  setup() {
    const { store } = usePinia()
  }
}
```

The `store` object provides access to the Pinia store and its APIs. You can use the `store.state` object to access the state, `store.get` to get a value from the store, `store.set` to set a value, and `store.reset` to reset the store.

You can also use the `store.watch` function to watch for changes in the store and the `store.on` function to register callbacks for events.

Here is an example of using the `store.watch` function to watch for changes in the store:

```js
import { usePinia } from 'pinia'

export default {
  setup() {
    const { store } = usePinia()

    store.watch(state => state.count, count => {
      console.log(`The count is now ${count}`)
    })
  }
}
```

## Output example


```
The count is now 0
```

## Helpful links

- [Pinia Documentation](https://pinia.netlify.app/)
- [Vue Composition API](https://composition-api.vuejs.org/)

onelinerhub: [How do I use Pinia with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-pinia-with-vue-js)