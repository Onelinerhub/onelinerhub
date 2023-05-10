# How do I add a variable to a string in Rust?
// plain

Adding a variable to a string in Rust is done using the `format!` macro. This macro allows you to insert variables into a string.

## Example code

```
let name = "John";
let message = format!("Hello, {}!", name);
println!("{}", message);
```

## Output example

```
Hello, John!
```

The code above consists of three parts:

1. `let name = "John";` - This declares a variable called `name` and assigns it the value `"John"`.

2. `let message = format!("Hello, {}!", name);` - This uses the `format!` macro to insert the value of the `name` variable into the string `"Hello, {}!"`.

3. `println!("{}", message);` - This prints the value of the `message` variable to the console.

## Helpful links

- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)

group: rust-variables