# How can I use a timer in Vue.js?
// plain

Using a timer in Vue.js is relatively easy. Here is an example of how to set a timer in Vue.js:

```
<template>
  <div>
    <h1>Timer Demo</h1>
    <p>{{ timer }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timer: 0
    }
  },
  created() {
    this.timer = setInterval(() => {
      this.timer++;
    }, 1000);
  },
  destroyed() {
    clearInterval(this.timer);
  }
}
</script>
```

This code will output a number that is incremented by 1 every second.

The code consists of the following parts:

1. The template: This is where the output of the timer is displayed.
2. The data: This is where the timer is initialized to 0.
3. The created hook: This is where the timer is set and it is executed when the component is created.
4. The destroyed hook: This is where the timer is cleared and it is executed when the component is destroyed.

For more information on using timers in Vue.js, please refer to the following links:

- [Vue.js Timers](https://vuejs.org/v2/guide/computed.html#Timers)
- [Vue.js Lifecycle Hooks](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)

onelinerhub: [How can I use a timer in Vue.js?](https://onelinerhub.com/vue.js/how-can-i-use-a-timer-in-vue-js)