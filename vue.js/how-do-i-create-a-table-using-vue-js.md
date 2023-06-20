# How do I create a table using Vue.js?
// plain

Creating a table using Vue.js is a straightforward process. To do this, you will need to create a template, create a script, and use the v-for directive to iterate through the data.

## Example code

```html
<template>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Age</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="person in people" :key="person.name">
        <td>{{person.name}}</td>
        <td>{{person.age}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  data() {
    return {
      people: [
        { name: 'John', age: 25 },
        { name: 'Jane', age: 32 },
        { name: 'Bob', age: 21 }
      ]
    }
  }
}
</script>
```

The code above will render the following table:

```
Name    Age
John    25
Jane    32
Bob     21
```

The template contains the HTML elements that will be used to create the table. The script contains the data that will be used to populate the table. The v-for directive is used to iterate through the data and create the table rows.

## Code explanation


1. `<template>` - This is the HTML element that contains the table elements.
2. `<thead>` - This is the table head element, which contains the column headers.
3. `<tr>` - This is the table row element, which contains the individual cells.
4. `<th>` - This is the table header element, which contains the column headers.
5. `<tbody>` - This is the table body element, which contains the table rows.
6. `v-for` - This is the Vue directive that is used to iterate through the data and create the table rows.
7. `data()` - This is the function that contains the data that will be used to populate the table.

## Helpful links

- [Vue.js Documentation - List Rendering](https://vuejs.org/v2/guide/list.html)
- [MDN - HTML Table Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)

onelinerhub: [How do I create a table using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-create-a-table-using-vue-js)