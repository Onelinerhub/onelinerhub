# How do I use Vue.js router-link?
// plain

Vue.js router-link is used to create an anchor tag that will link to a specified route. It is an important part of the Vue.js router and is used to navigate between different components.

## Example code

```
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
```

This code will create an anchor tag that links to the route specified in the `to` property. The `name` property specifies the name of the route and the `params` property is used to pass route parameters. In this example, the route name is `user` and the route parameter is `userId`.

## Code explanation

- `<router-link>`: The Vue.js router-link component
- `:to`: The property used to specify the route
- `name`: The route name
- `params`: The route parameters

## Helpful links
- [Vue.js Router-Link Documentation](https://router.vuejs.org/api/#router-link)

onelinerhub: [How do I use Vue.js router-link?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-router-link)