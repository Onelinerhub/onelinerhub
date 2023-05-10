# How do I use a range with a variable in Rust?
// plain

Using a range with a variable in Rust is a simple process. To do so, you must first declare a variable and assign it a value. Then, you can use the range syntax to create a range from the variable's value to a specified value. For example:

```
let x = 5;
let range = x..10;
```

This code creates a range from 5 to 10, using the variable `x`.

## Code explanation


- `let x = 5;` - This declares a variable `x` and assigns it the value of 5.
- `let range = x..10;` - This creates a range from the value of `x` to 10.

## Helpful links

- [Rust Range Syntax](https://doc.rust-lang.org/std/ops/struct.Range.html)

group: rust-variables