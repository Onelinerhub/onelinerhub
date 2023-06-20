# How do I use the v-if directive in Vue.js?
// plain

The `v-if` directive in Vue.js is used to conditionally render a piece of DOM based on a given expression. It is similar to an `if` statement in JavaScript, but with the added benefit of being able to render the DOM instead of just a boolean value.

For example, if we want to conditionally render a `<p>` element based on a boolean value, we can use the following code:

```
<div>
    <p v-if="showText">This text will be displayed if showText is true</p>
</div>
```

In the above example, the `<p>` element will only be rendered if the `showText` variable is `true`.

The `v-if` directive also supports `else` statements, which allows us to render a different piece of DOM if the expression evaluates to `false`. For example:

```
<div>
    <p v-if="showText">This text will be displayed if showText is true</p>
    <p v-else>This text will be displayed if showText is false</p>
</div>
```

In this example, if `showText` is `true`, the first `<p>` element will be rendered, and if `showText` is `false`, the second `<p>` element will be rendered.

The `v-if` directive is a powerful tool for conditionally rendering pieces of DOM in Vue.js.

## Code explanation

- `<p v-if="showText">`: This is the directive that is used to conditionally render the `<p>` element.
- `showText`: This is the variable that is used to determine whether the `<p>` element is rendered or not.
- `v-else`: This is the directive that is used to render a different piece of DOM if the expression evaluates to `false`.

## Helpful links
- [Vue.js Documentation - Conditional Rendering](https://vuejs.org/v2/guide/conditional.html)
- [Vue.js Directives](https://vuejs.org/v2/api/#v-if)

onelinerhub: [How do I use the v-if directive in Vue.js?](https://onelinerhub.com/vue.js/how-do-i-use-the-v-if-directive-in-vue-js)