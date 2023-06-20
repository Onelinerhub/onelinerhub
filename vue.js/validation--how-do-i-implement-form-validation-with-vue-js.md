# validation

How do I implement form validation with Vue.js?
// plain

Form validation is an important part of any web application. Vue.js provides an easy way to create form validation.

The following example code shows how to create a simple form validation with Vue.js:

```
<template>
  <form @submit.prevent="validateForm">
    <input type="text" v-model="name" />
    <button type="submit">Submit</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      name: ''
    }
  },
  methods: {
    validateForm() {
      if (this.name === '') {
        alert('Name is required!');
        return false;
      }
    }
  }
}
</script>
```

The code above uses the `v-model` directive to bind the input field to the `name` data property. The `submit` event is then intercepted and a method called `validateForm` is called. This method checks if the `name` property is empty and if it is, an alert is shown.

The parts of the code are:

- `<template>`: The markup for the form.
- `<input type="text" v-model="name" />`: An input field bound to the `name` data property using the `v-model` directive.
- `<button type="submit">Submit</button>`: A submit button to submit the form.
- `export default { ... }`: The Vue component code.
- `data() { return { name: '' } }`: The `name` data property set to an empty string.
- `methods: { validateForm() { ... } }`: The `validateForm` method which checks if the `name` property is empty and shows an alert if it is.

For more information about form validation with Vue.js, see the [official documentation](https://vuejs.org/v2/guide/forms.html).

onelinerhub: [validation

How do I implement form validation with Vue.js?](https://onelinerhub.com/vue.js/validation--how-do-i-implement-form-validation-with-vue-js)