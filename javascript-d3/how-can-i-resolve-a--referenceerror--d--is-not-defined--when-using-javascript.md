# How can I resolve a "ReferenceError: d3 is not defined" when using JavaScript?
// plain

The error "ReferenceError: d3 is not defined" occurs when the JavaScript code is trying to reference an object that is not defined. To resolve this error, the first step is to ensure that the d3 library is properly included in the code.

For example, if using a script tag, the following code can be used:

```
<script src="https://d3js.org/d3.v5.min.js"></script>
```

If the library is already included, the next step is to ensure that the code is properly referencing the object. This can be done by checking the syntax of the code and making sure that the object is being referenced correctly.

For example, the following code will reference the `d3` object:

```
let data = d3.csv("data.csv");
```

The code should be checked for any typos or incorrect syntax. If the code is correct, the error should be resolved.

## Code explanation


1. `<script src="https://d3js.org/d3.v5.min.js"></script>` - This code adds the d3 library to the page so that it can be referenced in the JavaScript code.
2. `let data = d3.csv("data.csv");` - This code references the d3 object and attempts to read a CSV file from the specified path.

List of ## Helpful links

- [D3.js](https://d3js.org/)
- [JavaScript ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_defined)

onelinerhub: [How can I resolve a "ReferenceError: d3 is not defined" when using JavaScript?](https://onelinerhub.com/javascript-d3/how-can-i-resolve-a--referenceerror--d--is-not-defined--when-using-javascript)