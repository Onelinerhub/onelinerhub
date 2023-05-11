# How to multiply matrices in Rust?
// plain

Multiplying matrices in Rust is done using the `mul` method from the `ndarray` crate. This method takes two matrices as arguments and returns the result of the multiplication.

## Example code

```rust
use ndarray::{arr2, Array2};

let a = arr2(&[[1, 2],
               [3, 4]]);
let b = arr2(&[[5, 6],
               [7, 8]]);

let c = a.mul(&b);
```

## Output example

```
[[19, 22],
 [43, 50]]
```

## Code explanation

- `use ndarray::{arr2, Array2};`: imports the `arr2` and `Array2` methods from the `ndarray` crate.
- `let a = arr2(&[[1, 2], [3, 4]]);`: creates a 2x2 matrix with the values `1, 2, 3, 4`.
- `let b = arr2(&[[5, 6], [7, 8]]);`: creates a 2x2 matrix with the values `5, 6, 7, 8`.
- `let c = a.mul(&b);`: multiplies the two matrices `a` and `b` and stores the result in `c`.

## Helpful links
- [ndarray crate](https://docs.rs/ndarray/0.13.0/ndarray/)
- [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)

group: rust-matrix

onelinerhub: [How to multiply matrices in Rust?](https://onelinerhub.com/rust/how-to-multiply-matrices-in-rust)