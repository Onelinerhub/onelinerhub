# How do I use Yup validation with ReactJS?
// plain

Yup is a JavaScript object schema validator and object parser. It can be used to validate and transform data in React applications. To use Yup with ReactJS, you need to install the yup package from npm.

```
npm install yup
```

Then, you can create a Yup schema for your form fields and use it to validate the form data. For example, if you want to validate a text field to ensure that it is not empty, you can use the following code:

```
import * as yup from 'yup';

const schema = yup.object().shape({
  textField: yup.string().required('This field is required')
});
```

Then, you can use the `validate()` method to validate the form data. For example:

```
const formData = {
  textField: ''
};

schema.validate(formData, { abortEarly: false })
  .then(() => {
    // validation successful
  })
  .catch(err => {
    // validation failed
  });
```

The `validate()` method will return a promise that resolves if the validation is successful, or rejects if the validation fails. You can use the `err` object to get the list of validation errors.

You can also use the `validateSync()` method to validate the form data synchronously. For example:

```
try {
  schema.validateSync(formData, { abortEarly: false });
  // validation successful
} catch (err) {
  // validation failed
}
```

## Helpful links

- [Yup Documentation](https://github.com/jquense/yup)
- [React Forms Validation with Yup](https://medium.com/@maks_rog/react-forms-validation-with-yup-8d7a6c9f5f6e)

onelinerhub: [How do I use Yup validation with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-yup-validation-with-reactjs)