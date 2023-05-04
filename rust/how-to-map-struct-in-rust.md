# How to map struct in Rust
// plain

Mapping a struct in Rust is done using the `.map()` method. This method takes a closure as an argument and applies it to each element of the struct. The closure can be used to modify the elements of the struct, or to create a new struct with the modified elements.

## Example

```rust
struct Point {
    x: i32,
    y: i32,
}

let points = vec![
    Point { x: 0, y: 0 },
    Point { x: 1, y: 5 },
    Point { x: 10, y: -3 },
];

let new_points = points.map(|p| Point { x: p.x, y: p.y + 1 });

println!("{:?}", new_points);
```
## Output example

```
[Point { x: 0, y: 1 }, Point { x: 1, y: 6 }, Point { x: 10, y: -2 }]
```

## Code explanation

- `struct Point { x: i32, y: i32, }`: This is the definition of the struct `Point`, which contains two fields, `x` and `y`, both of type `i32`.
- `let points = vec![ Point { x: 0, y: 0 }, Point { x: 1, y: 5 }, Point { x: 10, y: -3 }, ];`: This creates a vector of `Point` structs.
- `let new_points = points.map(|p| Point { x: p.x, y: p.y + 1 });`: This uses the `.map()` method to apply a closure to each element of the `points` vector. The closure creates a new `Point` struct with the same `x` value as the original, but with the `y` value incremented by 1.
- `println!("{:?}", new_points);`: This prints the modified vector of `Point` structs.

## Helpful links
- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Documentation - Vectors](https://doc.rust-lang.org/book/ch08-01-vectors.html)
- [Rust Documentation - Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)

group: rust-struct