# How to insert into a slice in Rust?
// plain

Inserting into a slice in Rust is done using the `insert()` method. This method takes two arguments, the index at which to insert the element and the element to be inserted.

## Example

```
let mut my_slice = [1, 2, 3];
my_slice.insert(1, 4);
```
## Output example

```
[1, 4, 2, 3]
```

## Code explanation

- `let mut my_slice = [1, 2, 3];`: This declares a mutable slice called `my_slice` with elements `1`, `2`, and `3`.
- `my_slice.insert(1, 4);`: This calls the `insert()` method on `my_slice`, inserting the element `4` at index `1`.

## Helpful links
- [Rust Documentation - Slice](https://doc.rust-lang.org/std/primitive.slice.html)
- [Rust Documentation - Vec::insert()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.insert)

group: rust-slice