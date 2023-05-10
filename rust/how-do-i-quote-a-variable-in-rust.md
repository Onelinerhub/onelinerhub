# How do I quote a variable in Rust?
// plain

In Rust, you can quote a variable by using the `format!` macro. This macro allows you to interpolate variables into a string.

For example:
```
let name = "John";
let message = format!("Hello, {}!", name);
println!("{}", message);
```

This code will output:
```
Hello, John!
```

The `format!` macro takes a string as its first argument, and then any number of variables to interpolate into the string. The variables are placed in the string using curly braces `{}` as placeholders.

The `println!` macro is then used to print the message to the console.

For more information, see the [Rust documentation on the format! macro](https://doc.rust-lang.org/std/macro.format.html).

group: rust-variables