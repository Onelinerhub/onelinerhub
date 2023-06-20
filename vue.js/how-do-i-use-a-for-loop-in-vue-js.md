# How do I use a for loop in Vue.js?
// plain

A `for` loop in Vue.js is used to iterate over an array or object. To use it, you need to define a `v-for` directive on the element you want to loop through.

Here is an example of a `for` loop in Vue.js:

```
<div id="example">
  <ul>
    <li v-for="item in items">{{ item }}</li>
  </ul>
</div>

<script>
  new Vue({
    el: '#example',
    data: {
      items: ['Apples', 'Bananas', 'Oranges']
    }
  })
</script>
```

The output of this code will be a list of items (Apples, Bananas, and Oranges).

## Code explanation


- `v-for` directive: This defines the loop and tells Vue.js what to loop through. In this example, it is set to `item in items`, which means it will loop through each item in the `items` array.
- `items` array: This is the array that contains the items that will be looped through. In this example, it contains strings (Apples, Bananas, and Oranges).
- `item` variable: This is the variable that will be used to reference each item in the array. In this example, it is referenced in the `{{ item }}` expression, which will display each item in the list.

## Helpful links

- [Vue.js Documentation - List Rendering](https://vuejs.org/v2/guide/list.html)
- [MDN Web Docs - for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

onelinerhub: [How do I use a for loop in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-a-for-loop-in-vue-js)