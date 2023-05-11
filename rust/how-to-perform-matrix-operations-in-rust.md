# How to perform matrix operations in Rust?
// plain

Matrix operations in Rust can be performed using the [nalgebra](https://nalgebra.org/) library. It provides a wide range of linear algebra operations, including matrix operations.

## Example

```rust
use nalgebra::{Matrix2, Vector2};

let a = Matrix2::new(1.0, 2.0,
                     3.0, 4.0);
let b = Vector2::new(5.0, 6.0);

let c = a * b;

println!("{:?}", c);
```
## Output example

```
Vector2 { x: 17.0, y: 39.0 }
```

The code above creates two matrices, `a` and `b`, and multiplies them together to produce a vector `c`. The `Matrix2` and `Vector2` types are provided by the nalgebra library. The `*` operator is used to perform the matrix multiplication. Finally, the `println!` macro is used to print the result.

Parts of the code:
- `use nalgebra::{Matrix2, Vector2};`: imports the `Matrix2` and `Vector2` types from the nalgebra library.
- `let a = Matrix2::new(1.0, 2.0, 3.0, 4.0);`: creates a 2x2 matrix with the given values.
- `let b = Vector2::new(5.0, 6.0);`: creates a 2-dimensional vector with the given values.
- `let c = a * b;`: performs matrix multiplication of `a` and `b` and stores the result in `c`.
- `println!("{:?}", c);`: prints the result of the matrix multiplication.

## Helpful links
- [nalgebra documentation](https://nalgebra.org/docs/)
- [Matrix multiplication in Rust](https://www.joshmcguigan.com/blog/matrix-multiplication-in-rust/)

group: rust-matrix

onelinerhub: [How to perform matrix operations in Rust?](https://onelinerhub.com/rust/how-to-perform-matrix-operations-in-rust)