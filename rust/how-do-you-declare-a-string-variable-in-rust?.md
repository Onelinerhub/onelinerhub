# How do you declare a string variable in Rust?
// plain

A string variable in Rust is declared using the `String` type. This type is provided by the standard library and is a growable, mutable string type.

## Example code

```
let my_string = String::new();
```

This code creates a new, empty `String` variable called `my_string`.

The code consists of two parts:
1. `let my_string` - This declares a variable called `my_string` using the `let` keyword.
2. `String::new()` - This creates a new `String` object and assigns it to the `my_string` variable.

For more information, see the [Rust documentation on Strings](https://doc.rust-lang.org/std/string/struct.String.html).