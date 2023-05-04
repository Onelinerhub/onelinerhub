# How to clone struct in Rust
// plain

Cloning a struct in Rust is a simple process. To clone a struct, you can use the `clone()` method. This method will create a deep copy of the struct, meaning that any changes made to the clone will not affect the original struct.

## Example

```rust
#[derive(Clone)]
struct Point {
    x: i32,
    y: i32,
}

let p1 = Point { x: 1, y: 2 };
let p2 = p1.clone();

println!("p1: {:?}", p1);
println!("p2: {:?}", p2);
```

## Output example

```
p1: Point { x: 1, y: 2 }
p2: Point { x: 1, y: 2 }
```

## Code explanation

- `#[derive(Clone)]` - This attribute is used to automatically implement the `clone()` method for the struct.
- `let p1 = Point { x: 1, y: 2 };` - This line creates a new instance of the `Point` struct.
- `let p2 = p1.clone();` - This line clones the `p1` instance and stores it in `p2`.
- `println!("p1: {:?}", p1);` - This line prints out the contents of `p1`.
- `println!("p2: {:?}", p2);` - This line prints out the contents of `p2`.

## Helpful links
- [Rust Documentation - Derive](https://doc.rust-lang.org/reference/attributes.html#derive)
- [Rust Documentation - Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html)

group: rust-struct