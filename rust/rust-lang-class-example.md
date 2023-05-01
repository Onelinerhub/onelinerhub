# Rust lang class example
// plain

A Rust lang class example is a program that demonstrates the basic concepts of the Rust programming language. Rust is a statically typed, memory-safe, and fast language that is used for systems programming.

Below is an example of a Rust class that defines a struct and a method:

```rust
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Point {
        Point { x, y }
    }

    fn distance(&self) -> f64 {
        let x_squared = (self.x as f64).powi(2);
        let y_squared = (self.y as f64).powi(2);
        (x_squared + y_squared).sqrt()
    }
}

fn main() {
    let p = Point::new(3, 4);
    println!("Distance from origin: {}", p.distance());
}
```

### Output

Distance from origin: 5.0

## Explanation of code parts:

1. `struct Point`: This defines a struct named Point with two fields, x and y, both of type i32.
2. `impl Point`: This defines an implementation block for the Point struct.
3. `fn new`: This is a method that takes two parameters, x and y, both of type i32, and returns a Point struct with those values.
4. `fn distance`: This is a method that takes a reference to a Point struct and returns the distance from the origin as a f64.
5. `let p = Point::new(3, 4)`: This creates a new Point struct with x = 3 and y = 4.
6. `println!("Distance from origin: {}", p.distance())`: This prints the distance from the origin to the console.

## Helpful links:

1. https://doc.rust-lang.org/book/ch05-00-structs.html
2. https://doc.rust-lang.org/rust-by-example/types/structs.html