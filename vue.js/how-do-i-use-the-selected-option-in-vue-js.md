# How do I use the selected option in Vue.js?
// plain

To use the selected option in Vue.js, you can use the `v-model` directive. This directive binds the value of a form input element to a data property in the component.

For example, the following code will bind the value of an input element to the `selectedOption` data property:

```html
<input type="text" v-model="selectedOption">
```

```javascript
data: {
  selectedOption: ''
}
```

The `v-model` directive will update the `selectedOption` data property when the user types in the input element.

You can also use the `v-model` directive to bind the value of a select element to a data property. For example, the following code will bind the value of a select element to the `selectedOption` data property:

```html
<select v-model="selectedOption">
  <option value="option1">Option 1</option>
  <option value="option2">Option 2</option>
</select>
```

```javascript
data: {
  selectedOption: ''
}
```

The `v-model` directive will update the `selectedOption` data property when the user selects an option from the select element.

## Helpful links
- [Vue.js - v-model](https://vuejs.org/v2/guide/forms.html#v-model)
- [MDN - HTML select element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)

onelinerhub: [How do I use the selected option in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-selected-option-in-vue-js)