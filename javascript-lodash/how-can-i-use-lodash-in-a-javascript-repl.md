# How can I use Lodash in a JavaScript REPL?
// plain

Using Lodash in a JavaScript REPL is easy. Here's an example:

```
> const _ = require('lodash');
> _.sum([4,2,8,6])
20
```

1. `const _ = require('lodash');` - This line imports the Lodash library into the REPL.
2. `_.sum([4,2,8,6])` - This line uses the Lodash `sum` function to add the numbers in the array.
3. `20` - This is the output of the Lodash `sum` function.

You can also use Lodash in the browser, by including the library in the HTML file. Here's an example:

```
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"></script>
<script>
  console.log(_.sum([4,2,8,6]));
</script>
```

1. `<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.15/lodash.min.js"></script>` - This line includes the Lodash library in the HTML file.
2. `console.log(_.sum([4,2,8,6]));` - This line uses the Lodash `sum` function to add the numbers in the array.
3. `20` - This is the output of the Lodash `sum` function.

For more information, check out the [Lodash documentation](https://lodash.com/docs/).

onelinerhub: [How can I use Lodash in a JavaScript REPL?](https://onelinerhub.com/javascript-lodash/how-can-i-use-lodash-in-a-javascript-repl)