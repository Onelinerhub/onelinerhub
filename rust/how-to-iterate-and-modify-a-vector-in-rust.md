# How to iterate and modify a vector in Rust
// plain

Iterating and modifying a vector in Rust is a simple process. To do so, you can use the `for` loop. The following example code block shows how to iterate and modify a vector:

```
let mut v = vec![1, 2, 3];

for i in &mut v {
    *i += 1;
}

println!("{:?}", v);
```

The output of the example code is:

```
[2, 3, 4]
```

The code consists of the following parts:

1. `let mut v = vec![1, 2, 3];` - This line creates a mutable vector `v` with the elements `1`, `2` and `3`.
2. `for i in &mut v {` - This line starts a `for` loop that iterates over the vector `v`.
3. `*i += 1;` - This line modifies the current element of the vector by incrementing it by `1`.
4. `println!("{:?}", v);` - This line prints the modified vector.

## Helpful links

- [Rust Book - Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [Rust Book - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-loops