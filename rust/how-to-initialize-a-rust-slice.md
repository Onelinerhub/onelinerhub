# How to initialize a Rust slice?
// plain

A Rust slice is a data structure that allows access to a contiguous sequence of elements in a collection. It can be initialized with the `[T; N]` syntax, where `T` is the type of the elements and `N` is the number of elements.

## Example

```
let my_slice: [i32; 5] = [1, 2, 3, 4, 5];
```
## Output example

```
[1, 2, 3, 4, 5]
```

## Code explanation

- `let`: the keyword used to declare a variable
- `my_slice`: the name of the variable
- `[i32; 5]`: the type of the variable, which is a slice of `i32`s with 5 elements
- `[1, 2, 3, 4, 5]`: the initial value of the variable, which is a literal array of 5 `i32`s

## Helpful links
- [Rust Slice Documentation](https://doc.rust-lang.org/std/primitive.slice.html)

group: rust-slice