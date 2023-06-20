# How do I implement a year picker using Vue.js?
// plain

To implement a year picker using Vue.js, we can use the `vue-date-picker` component.

The following example code can be used to create a year picker with the `vue-date-picker` component:

```
<template>
  <date-picker
    type="year"
    v-model="date"
  />
</template>

<script>
import DatePicker from 'vue-date-picker'

export default {
  components: {
    DatePicker
  },
  data () {
    return {
      date: new Date()
    }
  }
}
</script>
```

The output of the example code will be a year picker with the current year displayed.

## Code explanation


- `<template>`: This is the HTML template of the component.
- `<date-picker>`: This is the `vue-date-picker` component.
- `type="year"`: This is the attribute used to specify the type of the date picker as year.
- `v-model="date"`: This is the attribute used to bind the value of the date picker to the `date` variable.
- `import DatePicker from 'vue-date-picker'`: This is the code used to import the `vue-date-picker` component.
- `data () { return { date: new Date() } }`: This is the code used to initialize the `date` variable with the current date.

## Helpful links
- [Vue Date Picker](https://github.com/mengxiong10/vue2-datepicker)
- [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [How do I implement a year picker using Vue.js?](https://onelinerhub.com/vue.js/how-do-i-implement-a-year-picker-using-vue-js)