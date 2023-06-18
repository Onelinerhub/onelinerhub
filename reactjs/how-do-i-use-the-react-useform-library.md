# How do I use the React useForm library?
// plain

The React useForm library is a form library for React that helps you manage form state, validation, and submission. It provides a hook called `useForm` that you can use to create a form component.

```javascript
import { useForm } from 'react-hook-form';

const MyForm = () => {
  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        name="firstName"
        placeholder="First Name"
        ref={register({ required: true })}
      />
      <input
        name="lastName"
        placeholder="Last Name"
        ref={register({ required: true })}
      />
      <input type="submit" />
    </form>
  );
};
```

The code above creates a form with two input fields for first and last name. The `useForm` hook provides two properties: `register` and `handleSubmit`. The `register` property is used to register the input fields with the form, and the `handleSubmit` property is used to handle the form submission. The `register` property is used to validate the input fields, in this case, making sure they are both required.

When the form is submitted, the `onSubmit` function is called with the form data as a parameter. In the example, the data is logged to the console.

## Code explanation

- `import { useForm } from 'react-hook-form'`: imports the useForm hook
- `const { register, handleSubmit } = useForm()`: uses the useForm hook to get the register and handleSubmit properties
- `ref={register({ required: true })}`: registers the input field with the form and sets the required validation
- `onSubmit`: function that is called when the form is submitted
- `handleSubmit(onSubmit)`: handles the form submission and calls the onSubmit function

## Helpful links
- [React Hook Form](https://react-hook-form.com/)
- [useForm Documentation](https://react-hook-form.com/api#useForm)

onelinerhub: [How do I use the React useForm library?](https://onelinerhub.com/reactjs/how-do-i-use-the-react-useform-library)