# How do I use the emit function in Vue.js?
// plain

The `emit` function in Vue.js is used to send custom events from a child component to its parent component. It can be used to pass data from the child component to the parent.

For example, the following code will send an event named `child-event` from a child component to its parent.

```javascript
this.$emit('child-event', { data: 'some data' })
```

In the parent component, the event can be listened for using the `v-on` directive.

```javascript
<ChildComponent v-on:child-event="handleChildEvent" />
```

The `handleChildEvent` function can then be used to access the data from the event.

```javascript
methods: {
  handleChildEvent(data) {
    console.log('Received data from child:', data)
  }
}
```

## Output example


```
Received data from child: { data: 'some data' }
```

The `emit` function can also be used to pass data from the parent component to the child component. The parent component can send an event with `$emit` and the child component can listen for it with the `v-on` directive.

## Helpful links

- [Vue.js Documentation - Custom Events](https://vuejs.org/v2/guide/components-custom-events.html)

onelinerhub: [How do I use the emit function in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-emit-function-in-vue-js)