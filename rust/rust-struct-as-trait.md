# Rust struct as trait
// plain

A Rust struct can be used as a trait by implementing the trait for the struct. This allows the struct to use the methods and properties of the trait. For example, the following code defines a `Point` struct and implements the `Display` trait for it:

```rust
struct Point {
    x: i32,
    y: i32,
}

impl Display for Point {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

let p = Point { x: 3, y: 4 };
println!("{}", p);
```

## Output example

```
(3, 4)
```

The code above defines a `Point` struct with two fields `x` and `y`. The `impl Display for Point` block implements the `Display` trait for the `Point` struct. This allows the `Point` struct to use the `fmt` method of the `Display` trait. The `println!` macro then uses the `fmt` method to print the `Point` struct.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)

group: rust-struct