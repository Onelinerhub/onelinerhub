# How do I use Vue.js watch to monitor data changes?
// plain

Vue.js watch is a built-in feature that allows you to keep track of changes made to a data property. It is triggered every time the value of the data property changes and can be used to perform specific tasks.

Here is an example of how to use Vue.js watch:

```
<script>
  new Vue({
    data: {
      message: 'Hello World'
    },
    watch: {
      message: function (newMessage, oldMessage) {
        console.log('The message changed from ' + oldMessage + ' to ' + newMessage);
      }
    }
  })
</script>
```

In the example above, the `watch` property is used to monitor changes to the `message` data property. Whenever the value of `message` is changed, the function defined in `watch` will be triggered and the new and old values will be logged in the console.

## Code explanation


1. `data`: This property is used to define the data properties that will be monitored.
2. `watch`: This property is used to define the function that will be triggered whenever a data property changes.
3. `newMessage`: This parameter is used to store the new value of the data property.
4. `oldMessage`: This parameter is used to store the old value of the data property.
5. `console.log`: This is used to log a message to the console.

## Helpful links

- [Vue.js Documentation - Watchers](https://vuejs.org/v2/guide/computed.html#Watchers)
- [Vue.js Tutorial - Watchers](https://scrimba.com/g/gvuedev2)

onelinerhub: [How do I use Vue.js watch to monitor data changes?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-watch-to-monitor-data-changes)