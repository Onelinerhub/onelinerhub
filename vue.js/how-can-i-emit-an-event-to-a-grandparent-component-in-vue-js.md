# How can I emit an event to a grandparent component in Vue.js?
// plain

To emit an event to a grandparent component in Vue.js, you can use the `$emit` method. The `$emit` method allows you to trigger an event from a child component and pass data to the grandparent component. Here's an example:

```html
<template>
  <div>
    <grandparent-component>
      <parent-component>
        <child-component @emit-data="handleEmitData"/>
      </parent-component>
    </grandparent-component>
  </div>
</template>

<script>
export default {
  methods: {
    handleEmitData(data) {
      this.$emit('data-emitted', data);
    }
  }
}
</script>
```

The `handleEmitData` method in the example above is triggered when the `emit-data` event is emitted from the child component. The `handleEmitData` method then emits the `data-emitted` event with the data passed to it from the child component.

## Code explanation


1. `<grandparent-component>` - This is the grandparent component.
2. `<parent-component>` - This is the parent component, which is nested inside the grandparent component.
3. `<child-component @emit-data="handleEmitData"/>` - This is the child component, which is nested inside the parent component. The `@emit-data` attribute is used to bind the `emit-data` event to the `handleEmitData` method.
4. `handleEmitData(data) {...}` - This is the `handleEmitData` method, which is triggered when the `emit-data` event is emitted from the child component.
5. `this.$emit('data-emitted', data);` - This is the `$emit` method, which is used to emit the `data-emitted` event with the data passed to it from the child component.

## Helpful links

- [Vue.js Documentation - Events](https://vuejs.org/v2/guide/components-custom-events.html)
- [Vue.js Documentation - Emit](https://vuejs.org/v2/api/#vm-emit)

onelinerhub: [How can I emit an event to a grandparent component in Vue.js?](https://onelinerhub.com/vue.js/how-can-i-emit-an-event-to-a-grandparent-component-in-vue-js)