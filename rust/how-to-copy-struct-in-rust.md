# How to copy struct in Rust
// plain

Copying a struct in Rust is done using the `clone()` method. This method creates a deep copy of the struct, meaning that all fields are copied as well.

## Example

```rust
#[derive(Clone, Debug)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p1 = Point { x: 1, y: 2 };
    let p2 = p1.clone();
    println!("p1: {:?}", p1);
    println!("p2: {:?}", p2);
}
```

## Output example

```
p1: Point { x: 1, y: 2 }
p2: Point { x: 1, y: 2 }
```

## Code explanation

- `#[derive(Clone, Debug)]`: This line is necessary for the `clone()` method to work. It derives the `Clone` and `Debug` traits for the `Point` struct.
- `let p1 = Point { x: 1, y: 2 };`: This line creates a `Point` struct with the fields `x` and `y` set to `1` and `2` respectively.
- `let p2 = p1.clone();`: This line creates a deep copy of the `Point` struct `p1` and stores it in `p2`.
- `println!("p1: {:?}", p1);`: This line prints the `Point` struct `p1` to the console.
- `println!("p2: {:?}", p2);`: This line prints the `Point` struct `p2` to the console.

## Helpful links
- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Documentation - Traits](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Rust Documentation - Cloning](https://doc.rust-lang.org/std/clone/trait.Clone.html)

group: rust-struct