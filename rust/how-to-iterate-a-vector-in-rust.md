# How to iterate a vector in Rust
// plain

Iterating a vector in Rust is a simple process. The `for` loop is the most common way to iterate a vector. The following example code block shows how to iterate a vector of integers:

```
let v = vec![1, 2, 3];
for i in v {
    println!("{}", i);
}
```

This will output:
```
1
2
3
```

The ## Code explanation

- `let v = vec![1, 2, 3];`: This creates a vector of integers.
- `for i in v {`: This starts the `for` loop, which will iterate over each element in the vector.
- `println!("{}", i);`: This prints the current element of the vector.
- `}`: This ends the `for` loop.

## Helpful links
- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust Documentation - Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)

group: rust-loops