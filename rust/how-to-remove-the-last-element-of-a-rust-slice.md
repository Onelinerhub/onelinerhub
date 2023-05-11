# How to remove the last element of a Rust slice?
// plain

The last element of a Rust slice can be removed using the `pop()` method. This method removes the last element from the slice and returns it.

```rust
let mut my_slice = [1, 2, 3, 4];
let last_element = my_slice.pop();

println!("The last element is: {:?}", last_element);
```

## Output example

```
The last element is: Some(4)
```

The `pop()` method takes no arguments and returns an `Option<T>` where `T` is the type of the elements in the slice. If the slice is empty, `None` is returned.

## Code explanation

- `let mut my_slice = [1, 2, 3, 4];`: declares a mutable slice with four elements
- `let last_element = my_slice.pop();`: calls the `pop()` method on the slice to remove the last element
- `println!("The last element is: {:?}", last_element);`: prints the last element to the console

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - Option](https://doc.rust-lang.org/std/option/enum.Option.html)

group: rust-slice