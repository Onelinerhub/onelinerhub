# How to borrow struct field in Rust
// plain

Borrowing a struct field in Rust is done using the `&` operator. This operator creates a reference to the field, allowing it to be used without taking ownership of the struct.

Example:
```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 0, y: 0 };

    let borrowed_x = &point.x;

    println!("borrowed_x: {}", borrowed_x);
}
```

## Output example

```
borrowed_x: 0
```

## Code explanation

- `&` operator: creates a reference to the field
- `let point = Point { x: 0, y: 0 };`: creates a `Point` struct
- `let borrowed_x = &point.x;`: creates a reference to the `x` field of the `Point` struct
- `println!("borrowed_x: {}", borrowed_x);`: prints the value of the `x` field

## Helpful links
- [Rust Reference](https://doc.rust-lang.org/reference/index.html)
- [Rust Book - References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-borrow