# How do I use the Lodash includes method in JavaScript?
// plain

The Lodash includes method in JavaScript is used to determine whether an array or string contains a certain value. It is similar to the JavaScript indexOf method, but includes does not require the exact match of the value.

## Example

```
const array = [1,2,3,4,5];
_.includes(array, 3);
```
## Output example

```
true
```

The code above uses the Lodash includes method to check if the array contains the value 3. The code returns true, indicating that the array does contain the value 3.

The parts of the code are:

* `const array = [1,2,3,4,5];` - This declares a constant called array and sets its value to an array containing the numbers 1-5.

* `_.includes(array, 3);` - This uses the Lodash includes method to check if the array contains the value 3.

* `true` - This is the output of the code, indicating that the array does contain the value 3.

For more information on the Lodash includes method, see [the Lodash documentation](https://lodash.com/docs/4.17.15#includes).

onelinerhub: [How do I use the Lodash includes method in JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-the-lodash-includes-method-in-javascript)