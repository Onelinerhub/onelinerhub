# How do I use the jQuery when function?
// plain

The jQuery `when()` function is used to execute callback functions based on one or more objects, usually Deferred objects that represent asynchronous events. It is often used when handling multiple asynchronous operations, such as making multiple Ajax requests.

#### Example

```javascript
$.when(
    $.ajax("/page1.php"),
    $.ajax("/page2.php")
).done(function(page1, page2) {
    // Both requests are done
    console.log(page1, page2);
});
```

## Output example

```
<html>...</html> <html>...</html>
```

The `when()` function takes one or more Deferred objects as arguments. When all the Deferred objects are resolved, the `done()` callback is executed. The callback is passed the resolved values of all the Deferred objects as arguments.

#### List of Code Parts

- `$.when()` - This is the jQuery `when()` function, which takes one or more Deferred objects as arguments.
- `$.ajax()` - This is the jQuery `ajax()` function, which is used to make an asynchronous request.
- `done()` - This is the `done()` callback, which is executed when all the Deferred objects are resolved.

#### Relevant Links

- [jQuery.when() | jQuery API Documentation](https://api.jquery.com/jquery.when/)
- [jQuery.ajax() | jQuery API Documentation](https://api.jquery.com/jquery.ajax/)

onelinerhub: [How do I use the jQuery when function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-when-function)