# How do I use the get/set methods in Vue.js?
// plain

Using the get/set methods in Vue.js is a great way to create reactive data that can be used in your components. The get/set methods are part of the Vue.js reactivity system.

Here is an example of a get/set method being used in a Vue.js component:

```
<script>
export default {
    data() {
        return {
            message: ''
        }
    },
    computed: {
        reversedMessage: {
            get() {
                return this.message.split('').reverse().join('');
            },
            set(value) {
                this.message = value;
            }
        }
    }
}
</script>
```

In this example, the `reversedMessage` computed property is using a get/set method. The `get()` method is used to get the value of the `message` property, reverse it, and then return the reversed string. The `set()` method is used to set the value of the `message` property.

The parts of the code that are relevant to the get/set methods are:

- `computed`: this is an object that contains the get/set methods
- `get()`: this is the method that is used to get the value of the `message` property
- `set()`: this is the method that is used to set the value of the `message` property

For more information on the get/set methods in Vue.js, you can refer to the [Vue.js documentation](https://vuejs.org/v2/guide/computed.html#Computed-Setter).

onelinerhub: [How do I use the get/set methods in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-get-set-methods-in-vue-js)