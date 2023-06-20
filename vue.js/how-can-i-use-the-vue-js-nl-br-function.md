# How can I use the Vue.js nl2br function?
// plain

The Vue.js `nl2br` function is used to convert new line characters (`\n`) into HTML line break elements (`<br>`). This is useful for displaying text in a web page that may contain line breaks.

## Example

```
let str = "Hello\nWorld";
let result = this.$nl2br(str);
```
## Output example

```
Hello<br>World
```

The code above does the following:

1. Declares a `str` variable and assigns it the value `Hello\nWorld`.
2. Calls the `this.$nl2br` function with the `str` variable as its argument.
3. The `this.$nl2br` function converts the `\n` character in `str` into an HTML line break element `<br>`.

## Helpful links

- [Vue.js - Filters](https://vuejs.org/v2/api/#Filters)
- [Vue.js - nl2br](https://vuejs.org/v2/api/#nl2br)

onelinerhub: [How can I use the Vue.js nl2br function?](https://onelinerhub.com/vue.js/how-can-i-use-the-vue-js-nl-br-function)