# How to use struct as parameter in Rust
// plain

Structs can be used as parameters in Rust by passing them as references. This is done by using the `&` operator before the struct name. For example:

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 0 };

    print_point(&p);
}

fn print_point(point: &Point) {
    println!("Point x: {}, y: {}", point.x, point.y);
}
```

## Output example

```
Point x: 0, y: 0
```

## Code explanation


- `struct Point { x: i32, y: i32, }`: This is the definition of a struct called `Point` with two fields, `x` and `y`, both of type `i32`.

- `let p = Point { x: 0, y: 0 };`: This creates an instance of the `Point` struct with `x` and `y` set to `0`.

- `print_point(&p);`: This passes the `p` instance of `Point` to the `print_point` function as a reference.

- `fn print_point(point: &Point) {`: This is the definition of the `print_point` function, which takes a reference to a `Point` struct as a parameter.

- `println!("Point x: {}, y: {}", point.x, point.y);`: This prints out the `x` and `y` values of the `Point` struct passed as a parameter.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

group: rust-struct