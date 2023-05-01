# Rust lang class variable example
// plain

Class variables in Rust are declared using the `static` keyword. The following example shows how to declare a class variable in Rust:

```rust
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    // Declare a class variable
    static origin: Point = Point { x: 0, y: 0 };
}

fn main() {
    println!("The origin is: ({}, {})", Point::origin.x, Point::origin.y);
}
```

### Output

The origin is: (0, 0)

Explanation:

- `struct Point`: This declares a struct named `Point` with two fields, `x` and `y`.
- `static origin: Point = Point { x: 0, y: 0 };`: This declares a class variable named `origin` of type `Point` and initializes it with the value `Point { x: 0, y: 0 }`.
- `println!("The origin is: ({}, {})", Point::origin.x, Point::origin.y);`: This prints the value of the `origin` class variable.
- `Point::origin.x` and `Point::origin.y`: This is how you access the fields of a class variable.

## Helpful links:

- [Rust Documentation - Static Variables](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#static-variables)
- [Rust by Example - Structs](https://doc.rust-lang.org/rust-by-example/custom_types/structs.html)