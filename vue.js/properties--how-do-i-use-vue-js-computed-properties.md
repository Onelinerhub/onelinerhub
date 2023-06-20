# properties

How do I use Vue.js computed properties?
// plain

Computed properties in Vue.js are used to calculate values that are based on existing data in the Vue instance. This allows us to keep our data and logic separate, and make our code more concise and readable.

For example, we can use a computed property to calculate the total of a shopping cart:

```
<script>
  new Vue({
    data: {
      items: [
        { name: 'Apple', price: 10 },
        { name: 'Banana', price: 5 }
      ]
    },
    computed: {
      total() {
        let total = 0;
        this.items.forEach(item => {
          total += item.price;
        });
        return total;
      }
    }
  });
</script>
```

The output of this code would be `15`.

The code consists of the following parts:
1. `data`: An object containing the items to be added to the cart.
2. `computed`: An object containing the `total` computed property.
3. `total()`: A function that loops through the items in the `data` object and adds their prices together.
4. `return total`: The function returns the total of the items.

For more information, see the [Vue.js documentation](https://vuejs.org/v2/guide/computed.html).

onelinerhub: [properties

How do I use Vue.js computed properties?](https://onelinerhub.com/vue.js/properties--how-do-i-use-vue-js-computed-properties)