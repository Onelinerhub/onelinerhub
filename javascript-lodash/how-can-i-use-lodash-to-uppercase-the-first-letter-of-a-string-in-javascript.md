# How can I use Lodash to uppercase the first letter of a string in JavaScript?
// plain

Using Lodash, you can uppercase the first letter of a string in JavaScript with the `_.startCase()` method. This method will take a string or array of strings and capitalize the first letter of each word in the string.

## Example

```
let str = 'lodash is awesome';
let result = _.startCase(str);

console.log(result); // 'Lodash Is Awesome'
```

The output of the above code would be:
```
Lodash Is Awesome
```

The code consists of three parts:
1. The `let str = 'lodash is awesome'` statement declares a variable `str` and assigns it the value of the string `lodash is awesome`.
2. The `let result = _.startCase(str)` statement calls the Lodash `_.startCase()` method on the `str` variable and assigns the result to the `result` variable.
3. The `console.log(result)` statement logs the value of the `result` variable to the console.

For more information on the `_.startCase()` method, please refer to the [Lodash documentation](https://lodash.com/docs/4.17.15#startCase).

onelinerhub: [How can I use Lodash to uppercase the first letter of a string in JavaScript?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-to-uppercase-the-first-letter-of-a-string-in-javascript)