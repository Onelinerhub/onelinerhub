# How do I print a variable in Rust?
// plain

Printing a variable in Rust is done using the `println!` macro. This macro takes a format string and a list of arguments to print. The format string can contain placeholders for the arguments, which are then replaced with the values of the arguments.

## Example code

```
let x = 5;
println!("The value of x is {}", x);
```

## Output example

```
The value of x is 5
```

## Code explanation

- `println!`: The macro used to print a variable
- `"The value of x is {}"`: The format string, containing a placeholder for the argument
- `x`: The argument to be printed

## Helpful links
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)

group: rust-variables