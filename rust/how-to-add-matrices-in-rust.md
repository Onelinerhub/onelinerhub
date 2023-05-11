# How to add matrices in Rust?
// plain

Adding matrices in Rust is a simple task. The `zip()` method can be used to iterate over two matrices at the same time and add the corresponding elements. The following example code adds two matrices `a` and `b` and stores the result in `c`:

```rust
let a = vec![vec![1, 2], vec![3, 4]];
let b = vec![vec![5, 6], vec![7, 8]];
let mut c = vec![vec![0, 0], vec![0, 0]];

for (i, row) in a.iter().enumerate() {
    for (j, a_ij) in row.iter().enumerate() {
        c[i][j] = a_ij + b[i][j];
    }
}
```

The output of the example code is:

```
[[6, 8], [10, 12]]
```

The code consists of the following parts:

1. `let a = vec![vec![1, 2], vec![3, 4]];` creates a 2x2 matrix `a` with elements `1`, `2`, `3` and `4`.
2. `let b = vec![vec![5, 6], vec![7, 8]];` creates a 2x2 matrix `b` with elements `5`, `6`, `7` and `8`.
3. `let mut c = vec![vec![0, 0], vec![0, 0]];` creates a 2x2 matrix `c` with elements `0`, `0`, `0` and `0`.
4. `for (i, row) in a.iter().enumerate() {` iterates over the rows of matrix `a`.
5. `for (j, a_ij) in row.iter().enumerate() {` iterates over the elements of the current row of matrix `a`.
6. `c[i][j] = a_ij + b[i][j];` adds the corresponding elements of matrices `a` and `b` and stores the result in matrix `c`.

## Helpful links

- [Rust Documentation - Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)
- [Rust Documentation - Vectors](https://doc.rust-lang.org/stable/book/ch08-01-vectors.html)

group: rust-matrix

onelinerhub: [How to add matrices in Rust?](https://onelinerhub.com/rust/how-to-add-matrices-in-rust)