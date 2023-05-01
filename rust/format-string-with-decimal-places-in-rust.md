# Format string with decimal places in Rust
// plain

Formatting strings with decimal places in Rust can be done using the `format!` macro. This macro takes a format string as its first argument, followed by the values to be formatted. The format string can contain placeholders for the values, which can be used to specify the number of decimal places.

For example, the following code:

```
let x = 3.14159;
let y = format!("{:.2}", x);
println!("{}", y);
```

will output `3.14` as the value of `y`. The `.2` in the format string specifies that two decimal places should be used.

## Explanation:
1. `let x = 3.14159;` - This line declares a variable `x` and assigns it the value `3.14159`.
2. `let y = format!("{:.2}", x);` - This line uses the `format!` macro to format the value of `x` with two decimal places. The `.2` in the format string specifies that two decimal places should be used.
3. `println!("{}", y);` - This line prints the value of `y` to the console.

## Helpful links:
1. [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
2. [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)