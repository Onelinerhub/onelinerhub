# How do I use the Vue.js foreach loop to iterate over an array?
// plain

The `Vue.js` `foreach` loop is a powerful tool for iterating over an array. `foreach` creates a loop which iterates over each item in the array. To use `foreach` loop, you can use the following syntax:

```
<div v-for="item in arrayName">
  <!-- content -->
</div>
```

In the above example, the `v-for` directive is used to loop through the `arrayName` array and the `item` variable holds the current array element. The content inside the `div` element is repeated for each item in the array.

For example, if we have an array of numbers:

```
let numbers = [1,2,3,4];
```

We can use the `foreach` loop to iterate over the array and print out each number:

```
<div v-for="number in numbers">
  {{ number }}
</div>

```

The output of the above code would be:

```
1
2
3
4
```

Here is a list of parts of the `foreach` loop and a brief explanation of each:

- `v-for`: This is the directive used to create the `foreach` loop.
- `item`: This is the variable used to refer to the current array element.
- `arrayName`: This is the name of the array that you are looping through.

Here are some useful links for further reading:

- [Vue.js Array Change Detection](https://vuejs.org/v2/guide/list.html#Array-Change-Detection)
- [Vue.js v-for Directive](https://vuejs.org/v2/api/#v-for)

onelinerhub: [How do I use the Vue.js foreach loop to iterate over an array?](https://onelinerhub.com/vue.js/how-do-i-use-the-vue-js-foreach-loop-to-iterate-over-an-array)