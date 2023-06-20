# How do I use Yup with Vue.js?
// plain

Yup can be used with Vue.js to validate user input in forms. To use Yup with Vue.js, you need to install the `vuelidate` library.

```
npm install vuelidate
```

Once installed, you can use Yup with Vue.js in the following way:

```javascript
import { validationMixin } from 'vuelidate'
import { string } from 'yup'

export default {
  mixins: [validationMixin],
  validations: {
    username: {
      required: string().required('Username is required'),
      minLength: string().min(4, 'Username must be at least 4 characters long')
    }
  }
}
```

The `validationMixin` provides a `$v` object which can be used to access the validation state of the form. The `string()` function from Yup is used to create a validation schema for the `username` input. The `required` and `minLength` functions are used to set the validation rules for the `username` input.

## Code explanation

- `validationMixin`: provides a `$v` object which can be used to access the validation state of the form
- `string()`: creates a validation schema for the `username` input
- `required`: sets the validation rule that the `username` input is required
- `minLength`: sets the validation rule that the `username` input must be at least 4 characters long

## Helpful links
- [Yup Documentation](https://github.com/jquense/yup)
- [Vuelidate Documentation](https://monterail.github.io/vuelidate/)

onelinerhub: [How do I use Yup with Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-yup-with-vue-js)