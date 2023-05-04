# How to get struct value in Rust
// plain

Structs are a way to create custom data types in Rust. To get the value of a struct, you can use the dot operator (`.`).

## Example

```
struct Point {
    x: i32,
    y: i32,
}

let p = Point { x: 10, y: 20 };

println!("x = {}", p.x);
println!("y = {}", p.y);
```
## Output example

```
x = 10
y = 20
```

## Code explanation

- `struct Point { x: i32, y: i32, }`: This creates a struct called `Point` with two fields, `x` and `y`, both of type `i32`.
- `let p = Point { x: 10, y: 20 };`: This creates a `Point` instance with `x` set to `10` and `y` set to `20`.
- `println!("x = {}", p.x);`: This prints the value of `x` from the `Point` instance `p`.
- `println!("y = {}", p.y);`: This prints the value of `y` from the `Point` instance `p`.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Dot Operator](https://doc.rust-lang.org/book/ch06-02-match.html#the-dot-operator)

group: rust-struct