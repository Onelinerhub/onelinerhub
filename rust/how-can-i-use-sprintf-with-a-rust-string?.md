# How can I use sprintf with a Rust string?
// plain

You can use `sprintf` with a Rust string by using the `format!` macro. This macro takes a format string and a list of arguments, and returns a `String` object.

## Example code

```
let name = "John";
let age = 30;
let message = format!("{} is {} years old", name, age);
println!("{}", message);
```

## Output example

```
John is 30 years old
```

## Code explanation

- `let name = "John";`: This declares a variable `name` and assigns it the value `"John"`.
- `let age = 30;`: This declares a variable `age` and assigns it the value `30`.
- `let message = format!("{} is {} years old", name, age);`: This uses the `format!` macro to create a `String` object with the format string `"{} is {} years old"` and the arguments `name` and `age`.
- `println!("{}", message);`: This prints the `String` object `message` to the console.

## Helpful links
- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)