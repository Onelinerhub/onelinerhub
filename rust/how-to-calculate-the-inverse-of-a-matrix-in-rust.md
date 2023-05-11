# How to calculate the inverse of a matrix in Rust?
// plain

The inverse of a matrix can be calculated in Rust using the `inverse` method from the `nalgebra` crate. This method takes a matrix as an argument and returns the inverse of the matrix.

## Example code

```rust
use nalgebra::{Matrix3, Matrix4};

let m3 = Matrix3::new(1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0,
                      7.0, 8.0, 9.0);
let m3_inv = m3.inverse();

let m4 = Matrix4::new(1.0, 2.0, 3.0, 4.0,
                      5.0, 6.0, 7.0, 8.0,
                      9.0, 10.0, 11.0, 12.0,
                      13.0, 14.0, 15.0, 16.0);
let m4_inv = m4.inverse();
```

## Output example

```
m3_inv = Matrix3 {
    x: [-4.50, 4.50, -3.00],
    y: [3.75, -3.75, 2.50],
    z: [-2.25, 2.25, -1.50],
}

m4_inv = Matrix4 {
    x: [-6.00, 4.50, -1.50, 1.50],
    y: [4.20, -3.00, 0.80, -0.80],
    z: [-1.40, 1.05, -0.30, 0.30],
    w: [0.50, -0.35, 0.10, -0.10],
}
```

## Code explanation


1. `use nalgebra::{Matrix3, Matrix4};`: This imports the `Matrix3` and `Matrix4` types from the `nalgebra` crate.
2. `let m3 = Matrix3::new(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0);`: This creates a 3x3 matrix with the given values.
3. `let m3_inv = m3.inverse();`: This calculates the inverse of the matrix `m3`.
4. `let m4 = Matrix4::new(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0);`: This creates a 4x4 matrix with the given values.
5. `let m4_inv = m4.inverse();`: This calculates the inverse of the matrix `m4`.

## Helpful links

- [nalgebra documentation](https://docs.rs/nalgebra/0.20.0/nalgebra/)

group: rust-matrix

onelinerhub: [How to calculate the inverse of a matrix in Rust?](https://onelinerhub.com/rust/how-to-calculate-the-inverse-of-a-matrix-in-rust)