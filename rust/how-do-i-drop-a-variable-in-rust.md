# How do I drop a variable in Rust?
// plain

Dropping a variable in Rust is done using the `drop` function. This function takes a reference to a variable and deallocates the memory associated with it.

## Example

```
let x = Box::new(5);
drop(x);
```

This code will deallocate the memory associated with the variable `x`.

## Code explanation


- `let x = Box::new(5);`: This line creates a new variable `x` and allocates memory for it.
- `drop(x);`: This line calls the `drop` function, which takes a reference to the variable `x` and deallocates the memory associated with it.

## Helpful links

- [Rust Documentation - The Drop Trait](https://doc.rust-lang.org/std/ops/trait.Drop.html)

group: rust-variables