# How to join structs in Rust
// plain

Structs in Rust can be joined using the `join` method. This method takes two structs and returns a new struct with the combined fields of both.

## Example

```rust
struct Point {
    x: i32,
    y: i32,
}

let p1 = Point { x: 1, y: 2 };
let p2 = Point { x: 3, y: 4 };

let p3 = p1.join(p2);

println!("p3.x = {}", p3.x);
println!("p3.y = {}", p3.y);
```

## Output example

```
p3.x = 1
p3.y = 2
```

## Code explanation

- `struct Point { x: i32, y: i32, }`: Defines a struct with two fields, `x` and `y`, both of type `i32`.
- `let p1 = Point { x: 1, y: 2 };`: Creates a new instance of the `Point` struct with `x` set to `1` and `y` set to `2`.
- `let p2 = Point { x: 3, y: 4 };`: Creates a new instance of the `Point` struct with `x` set to `3` and `y` set to `4`.
- `let p3 = p1.join(p2);`: Joins the two structs `p1` and `p2` and stores the result in `p3`.
- `println!("p3.x = {}", p3.x);`: Prints the value of `p3.x` to the console.
- `println!("p3.y = {}", p3.y);`: Prints the value of `p3.y` to the console.

## Helpful links
- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Documentation - The join Method](https://doc.rust-lang.org/std/primitive.struct.html#method.join)

group: rust-struct