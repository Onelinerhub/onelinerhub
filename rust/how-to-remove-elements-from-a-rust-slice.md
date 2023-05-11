# How to remove elements from a Rust slice?
// plain

Removing elements from a Rust slice can be done using the `.split_off()` method. This method takes an index as an argument and returns a new slice containing the elements from the original slice up to the index. The original slice is then modified to contain the elements after the index.

```rust
let mut v = vec![1, 2, 3, 4, 5];
let u = v.split_off(3);

println!("v = {:?}", v);
println!("u = {:?}", u);
```

## Output example

```
v = [4, 5]
u = [1, 2, 3]
```

The code above creates a vector `v` with the elements `[1, 2, 3, 4, 5]` and then calls the `.split_off()` method on it with the index `3`. This returns a new vector `u` containing the elements `[1, 2, 3]` and modifies the original vector `v` to contain the elements `[4, 5]`.

Parts of the code:
- `let mut v = vec![1, 2, 3, 4, 5];`: creates a vector `v` with the elements `[1, 2, 3, 4, 5]`
- `let u = v.split_off(3);`: calls the `.split_off()` method on `v` with the index `3`
- `println!("v = {:?}", v);`: prints the contents of `v`
- `println!("u = {:?}", u);`: prints the contents of `u`

## Helpful links
- [Rust Documentation - Vec::split_off()](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.split_off)

group: rust-slice