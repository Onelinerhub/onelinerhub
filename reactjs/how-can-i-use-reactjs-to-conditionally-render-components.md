# How can I use ReactJS to conditionally render components?
// plain

ReactJS provides a powerful way of conditionally rendering components using the ternary operator. This operator allows you to check a condition and render different components depending on the outcome.

For example, if you wanted to render a component if a user is logged in, you could use the following code:

```
{isLoggedIn ? <MyComponent /> : null}
```

This code would check the `isLoggedIn` condition and if it evaluates to `true` it would render the `MyComponent` component. If the `isLoggedIn` condition evaluates to `false` then nothing would be rendered.

You can also use the `&&` operator to conditionally render components:

```
{isLoggedIn && <MyComponent />}
```

This code would check the `isLoggedIn` condition and if it evaluates to `true` it would render the `MyComponent` component. If the `isLoggedIn` condition evaluates to `false` then nothing would be rendered.

You can also use the `if-else` statement to conditionally render components:

```
{
  if (isLoggedIn) {
    return <MyComponent />;
  } else {
    return null;
  }
}
```

This code would check the `isLoggedIn` condition and if it evaluates to `true` it would render the `MyComponent` component. If the `isLoggedIn` condition evaluates to `false` then nothing would be rendered.

You can also use the `switch` statement to conditionally render components:

```
{
  switch (isLoggedIn) {
    case true:
      return <MyComponent />;
    default:
      return null;
  }
}
```

This code would check the `isLoggedIn` condition and if it evaluates to `true` it would render the `MyComponent` component. If the `isLoggedIn` condition evaluates to `false` then nothing would be rendered.

## Helpful links
- [ReactJS Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)
- [Ternary Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
- [Logical && Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators#Logical_AND)
- [if-else Statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- [switch Statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

onelinerhub: [How can I use ReactJS to conditionally render components?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-conditionally-render-components)