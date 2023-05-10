# How do I insert a variable into a string in Rust?
// plain

You can insert a variable into a string in Rust using the `format!` macro. This macro allows you to insert variables into a string using the `{}` placeholder. For example:

```
let name = "John";
let message = format!("Hello, {}!", name);
```

This will output `Hello, John!`.

The `format!` macro takes the following parts:

- `format!`: The macro itself.
- `"Hello, {}!"`: The string with the `{}` placeholder.
- `name`: The variable to be inserted into the string.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/macro.format.html).

group: rust-variables