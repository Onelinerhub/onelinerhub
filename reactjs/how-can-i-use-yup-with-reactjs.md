# How can I use Yup with ReactJS?
// plain

Yup is a JavaScript object schema validator and object parser. It can be used to validate and transform data in React applications.

To use Yup with ReactJS, you need to install the Yup package using npm or yarn.

```
npm install yup
```

Once the package is installed, you can import it into your React component and use it to validate and transform data.

```
import * as yup from 'yup';

const schema = yup.object().shape({
  name: yup.string().required(),
  age: yup.number().min(18).required(),
});
```

The code above creates a Yup schema that validates and transforms data. The `name` field is required and must be a string, while the `age` field is required and must be a number greater than or equal to 18.

You can then use the schema to validate data.

```
const data = {
  name: 'John Doe',
  age: 25
};

schema.isValid(data).then(valid => {
  if (valid) {
    console.log('Data is valid!');
  } else {
    console.log('Data is invalid!');
  }
});
```

The code above checks if the data is valid according to the schema, and prints a message to the console.

You can also use the schema to transform the data:

```
schema.cast(data).then(transformedData => {
  console.log(transformedData);
});
```

The code above transforms the data according to the schema, and prints the transformed data to the console.

## Helpful links
- [Yup Documentation](https://github.com/jquense/yup)
- [React Documentation](https://reactjs.org/docs/getting-started.html)

onelinerhub: [How can I use Yup with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-yup-with-reactjs)