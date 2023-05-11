# How to split a Rust slice into chunks?
// plain

Splitting a Rust slice into chunks can be done using the `chunks()` method. This method takes a parameter `size` which is the size of each chunk.

## Example code

```
let slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let chunks = slice.chunks(3);
```

## Output example

```
[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

## Code explanation

- `let slice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];`: This creates a slice of 10 elements.
- `let chunks = slice.chunks(3);`: This calls the `chunks()` method on the slice with the parameter `size` set to 3.
- `chunks()`: This is the method used to split the slice into chunks.

## Helpful links
- [Rust Documentation - Chunks](https://doc.rust-lang.org/std/primitive.slice.html#method.chunks)

group: rust-slice