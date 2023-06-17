# How do I check if jQuery is enabled?
// plain

To check if jQuery is enabled on a webpage, you can use the following code:

```
if (typeof jQuery == 'undefined') {
   // jQuery is not loaded
   alert("jQuery is not enabled");
}
else {
   // jQuery is loaded
   alert("jQuery is enabled");
}
```

The output of this code will be an alert box that will show either "jQuery is not enabled" or "jQuery is enabled".

The code works by checking the type of the variable `jQuery`. If the type is `undefined`, then jQuery is not loaded. Otherwise, jQuery is loaded.

The code consists of the following parts:

1. `if (typeof jQuery == 'undefined')`: This is the condition that checks if the type of `jQuery` is `undefined`.
2. `alert("jQuery is not enabled")`: This is the code that will be executed if the condition is true. It will display an alert box that says "jQuery is not enabled".
3. `else`: This is the code that will be executed if the condition is false.
4. `alert("jQuery is enabled")`: This is the code that will be executed if the condition is false. It will display an alert box that says "jQuery is enabled".

For more information about how to check if jQuery is enabled, please refer to the following links:

- [How to check if jQuery is enabled](https://stackoverflow.com/questions/5701122/how-to-check-if-jquery-is-enabled)
- [Checking if jQuery is enabled](https://www.sitepoint.com/checking-if-jquery-is-enabled/)

onelinerhub: [How do I check if jQuery is enabled?](https://onelinerhub.com/jquery/how-do-i-check-if-jquery-is-enabled)