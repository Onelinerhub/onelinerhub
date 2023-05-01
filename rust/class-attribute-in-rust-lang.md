# Class attribute in Rust lang
// plain

Class attributes in Rust lang are used to store data associated with a particular type. They are declared using the keyword `static` and can be accessed using the double colon (::) operator.

## Code example:

```rust
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    // Declare a static attribute
    static origin: Point = Point { x: 0, y: 0 };
}

fn main() {
    // Access the static attribute
    println!("The origin is at ({}, {})", Point::origin.x, Point::origin.y);
}
```

### Output

The origin is at (0, 0)

## Code explanation of code parts:

1. `struct Point`: This declares a struct type named Point which contains two fields, x and y.
2. `static origin: Point = Point { x: 0, y: 0 };`: This declares a static attribute named origin of type Point and assigns it the value of a Point instance with x and y set to 0.
3. `Point::origin`: This accesses the static attribute origin.
4. `println!("The origin is at ({}, {})", Point::origin.x, Point::origin.y);`: This prints out the origin's x and y coordinates.

## Helpful links:

1. https://doc.rust-lang.org/book/ch05-01-defining-structs.html
2. https://doc.rust-lang.org/book/ch05-03-method-syntax.html