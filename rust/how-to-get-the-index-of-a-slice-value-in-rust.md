# How to get the index of a slice value in Rust?
// plain

The `index()` method can be used to get the index of a slice value in Rust.

## Example code

```
let arr = [1, 2, 3, 4, 5];
let index = arr.index(2);
println!("The index of 2 is {}", index);
```

## Output example

```
The index of 2 is 1
```

## Code explanation

- `let arr = [1, 2, 3, 4, 5];`: This line declares an array of integers.
- `let index = arr.index(2);`: This line calls the `index()` method on the array, passing in the value 2 as an argument.
- `println!("The index of 2 is {}", index);`: This line prints the index of the value 2.

## Helpful links
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#arrays)
- [Rust Documentation - Index Method](https://doc.rust-lang.org/std/primitive.slice.html#method.index)

group: rust-slice