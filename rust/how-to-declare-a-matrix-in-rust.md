# How to declare a matrix in Rust?
// plain

A matrix can be declared in Rust using a two-dimensional array. The following example code block shows how to declare a 3x3 matrix:

```
let matrix: [[i32; 3]; 3] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];
```

The output of the above code is:

```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

The code consists of the following parts:

- `let`: This is a keyword used to declare a variable.
- `matrix`: This is the name of the variable.
- `[[i32; 3]; 3]`: This is the type of the variable. It is a two-dimensional array of type `i32` with 3 elements in each row.
- `[...]`: This is the value of the variable. It is an array of 3 arrays, each containing 3 elements.

## Helpful links

- [Rust Documentation - Arrays](https://doc.rust-lang.org/book/ch03-02-data-types.html#arrays)

group: rust-matrix

onelinerhub: [How to declare a matrix in Rust?](https://onelinerhub.com/rust/how-to-declare-a-matrix-in-rust)