# How to embed struct in Rust
// plain

Structs are a way to create custom data types in Rust. They allow you to group related data together and give it a name. To embed a struct in Rust, you must first define the struct and then use the `struct` keyword to declare it.

## Example code

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 0, y: 0 };
    println!("Point coordinates: ({}, {})", point.x, point.y);
}
```

## Output example

```
Point coordinates: (0, 0)
```

## Code explanation

- `struct Point { x: i32, y: i32, }`: This defines the struct with two fields, `x` and `y`, both of type `i32`.
- `let point = Point { x: 0, y: 0 };`: This creates an instance of the `Point` struct with the given values for `x` and `y`.
- `println!("Point coordinates: ({}, {})", point.x, point.y);`: This prints out the coordinates of the `Point` instance.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Enums and Structs](https://doc.rust-lang.org/rust-by-example/custom_types/enum_struct.html)

group: rust-struct