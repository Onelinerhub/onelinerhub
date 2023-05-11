# How to get the bytes of a Rust slice?
// plain

To get the bytes of a Rust slice, you can use the `as_bytes()` method. This method returns a `&[u8]` slice which contains the bytes of the original slice.

## Example

```
let my_slice = [1, 2, 3];
let bytes = my_slice.as_bytes();
```
## Output example

```
[1, 2, 3]
```

## Code explanation

- `let my_slice = [1, 2, 3];`: This creates a slice containing the numbers 1, 2, and 3.
- `let bytes = my_slice.as_bytes();`: This calls the `as_bytes()` method on the `my_slice` slice, which returns a `&[u8]` slice containing the bytes of the original slice.

## Helpful links
- [Rust Documentation - as_bytes()](https://doc.rust-lang.org/std/primitive.slice.html#method.as_bytes)

group: rust-slice