# How to append to a Rust slice?
// plain

Appending to a Rust slice can be done using the `push()` method. This method takes a single argument and adds it to the end of the slice.

```rust
let mut my_slice = vec![1, 2, 3];
my_slice.push(4);
println!("{:?}", my_slice);
```

## Output example

```
[1, 2, 3, 4]
```

The `push()` method takes a single argument and adds it to the end of the slice:
- `my_slice`: The slice to which the element should be appended.
- `4`: The element to be appended to the slice.

## Helpful links
- [Rust Documentation - Vec::push()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.push)

group: rust-slice