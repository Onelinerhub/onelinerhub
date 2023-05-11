# How to iterate over a Rust slice with an index?
// plain

Iterating over a Rust slice with an index can be done using a `for` loop. The loop will iterate over each element in the slice and provide the index of the element as well.

```rust
let my_slice = [1, 2, 3, 4];

for (index, element) in my_slice.iter().enumerate() {
    println!("Element at index {} is {}", index, element);
}
```

## Output example

```
Element at index 0 is 1
Element at index 1 is 2
Element at index 2 is 3
Element at index 3 is 4
```

## Code explanation

- `let my_slice = [1, 2, 3, 4];`: This declares a slice containing the elements 1, 2, 3, and 4.
- `for (index, element) in my_slice.iter().enumerate()`: This is the `for` loop which will iterate over each element in the slice. The `enumerate()` method will provide the index of the element as well.
- `println!("Element at index {} is {}", index, element);`: This prints out the index and element of the current iteration.

## Helpful links
- [Rust Documentation - Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)

group: rust-slice