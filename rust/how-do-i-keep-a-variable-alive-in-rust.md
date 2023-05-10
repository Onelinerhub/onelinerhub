# How do I keep a variable alive in Rust?
// plain

Variables in Rust are kept alive by using the `std::mem::drop` function. This function takes a reference to a variable and deallocates the memory associated with it. This ensures that the variable is no longer accessible and can no longer be used.

## Example

```
let mut x = 5;
std::mem::drop(&mut x);
```

This code will deallocate the memory associated with the variable `x`, making it no longer accessible.

## Code explanation


- `let mut x = 5;`: This line declares a mutable variable `x` and assigns it the value `5`.
- `std::mem::drop(&mut x);`: This line calls the `std::mem::drop` function, passing a reference to the variable `x` as an argument. This deallocates the memory associated with `x`, making it no longer accessible.

## Helpful links

- [std::mem::drop](https://doc.rust-lang.org/std/mem/fn.drop.html)

group: rust-variables