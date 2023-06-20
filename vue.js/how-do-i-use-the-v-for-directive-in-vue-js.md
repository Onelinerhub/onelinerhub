# How do I use the v-for directive in Vue.js?
// plain

The `v-for` directive is used in Vue.js to render a list of items based on an array. It works similarly to a `for` loop in JavaScript.

## Example code

```html
<div id="app">
  <ul>
    <li v-for="item in items">{{ item.text }}</li>
  </ul>
</div>

<script>
  new Vue({
    el: '#app',
    data: {
      items: [
        { text: 'Foo' },
        { text: 'Bar' },
        { text: 'Baz' }
      ]
    }
  })
</script>
```

## Output example

```
Foo
Bar
Baz
```

The code consists of the following parts:

1. `<div id="app">`: This is the root element for the Vue instance.
2. `<ul>`: This is the unordered list element which will contain the items.
3. `<li v-for="item in items">`: This is the directive which tells Vue to loop through the `items` array and create a list item for each item in the array.
4. `{{ item.text }}`: This is the text that will be displayed for each list item.

## Helpful links
- [Vue.js Documentation - List Rendering](https://vuejs.org/v2/guide/list.html)
- [Vue.js Documentation - Directives](https://vuejs.org/v2/guide/syntax.html#Directives)

onelinerhub: [How do I use the v-for directive in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-v-for-directive-in-vue-js)