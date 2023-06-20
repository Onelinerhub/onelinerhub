# How do I use Vue.js watchers to detect changes in data?
// plain

Watchers are an important feature of Vue.js which allow you to detect changes in data. Watchers are declared inside the `watch` option of a Vue instance, and they are triggered whenever the value of a reactive property changes.

For example, the following code uses a watcher to detect changes in the `message` data property:
```
<script>
  new Vue({
    el: '#app',
    data: {
      message: 'Hello World!'
    },
    watch: {
      message: function (newVal, oldVal) {
        console.log('Message changed from ' + oldVal + ' to ' + newVal);
      }
    }
  });
</script>
```

When the value of `message` changes, the watcher's callback function will be invoked, and the output will look like this:
```
Message changed from Hello World! to Hi there!
```

The callback function receives two parameters: `newVal` which is the new value of the property, and `oldVal` which is the previous value of the property.

## Code explanation


- `watch`: This is the option used to declare a watcher in a Vue instance.
- `message`: This is the data property which is being watched.
- `function (newVal, oldVal)`: This is the callback function which is invoked when the value of `message` changes. It receives two parameters: `newVal` which is the new value of the property, and `oldVal` which is the previous value of the property.
- `console.log`: This is used to log the message when the watcher is triggered.

## Helpful links

- [Vue.js Watchers Documentation](https://vuejs.org/v2/guide/computed.html#Watchers)
- [Vue.js Watchers Tutorial](https://scotch.io/tutorials/vue-watchers-deep-dive)

onelinerhub: [How do I use Vue.js watchers to detect changes in data?](https://onelinerhub.com/vue.js/how-do-i-use-vue-js-watchers-to-detect-changes-in-data)