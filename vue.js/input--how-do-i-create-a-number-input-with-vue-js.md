# input

How do I create a number input with Vue.js?
// plain

You can create a number input with Vue.js using the `v-model` directive. The `v-model` directive binds the value of the input to a data property, which can then be used to perform calculations or update other parts of the page.

## Example code

```
<input type="number" v-model="myNumber">
```

This code will create an input field with the type set to `number`, and the value of the field will be bound to the `myNumber` data property.

The `v-model` directive can also be used to bind the input value to a computed property, which can be used to perform calculations or other logic.

## Example code

```
<input type="number" v-model="myComputedNumber">

...

computed: {
  myComputedNumber: function () {
    return this.myNumber * 2;
  }
}
```

The code above will create an input field with the type set to `number`, and the value of the field will be bound to the `myComputedNumber` computed property. This computed property will return the value of `myNumber` multiplied by two.

## Code explanation

- `<input type="number" v-model="myNumber">`: This creates an input field with the type set to `number`, and the value of the field will be bound to the `myNumber` data property.
- `v-model="myComputedNumber"`: This binds the value of the input field to the `myComputedNumber` computed property.
- `myComputedNumber: function () { return this.myNumber * 2; }`: This computed property returns the value of `myNumber` multiplied by two.

## Helpful links
- [Vue.js Guide: Forms and Inputs](https://vuejs.org/v2/guide/forms.html)
- [Vue.js API: v-model](https://vuejs.org/v2/api/#v-model)

onelinerhub: [input

How do I create a number input with Vue.js?](https://onelinerhub.com/vue.js/input--how-do-i-create-a-number-input-with-vue-js)