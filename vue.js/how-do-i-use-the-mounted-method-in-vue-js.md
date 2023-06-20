# How do I use the mounted method in Vue.js?
// plain

The `mounted` method is a Vue.js lifecycle hook that is called after the instance has been mounted to the DOM. This hook can be used to perform any necessary setup that requires the instance to be fully mounted and ready to go.

## Example code

```
<script>
export default {
  mounted() {
    console.log('Instance is mounted!')
  }
}
</script>
```

## Output example
 `Instance is mounted!`

## Code explanation

- `mounted()`: The `mounted` method is a lifecycle hook that is called after the instance has been mounted to the DOM.
- `console.log('Instance is mounted!')`: This line of code logs the message `Instance is mounted!` to the console.

## Helpful links
- [Vue.js Lifecycle Hooks Documentation](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)

onelinerhub: [How do I use the mounted method in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-mounted-method-in-vue-js)