# Rust lang class api
// plain

Rust is a statically typed, multi-paradigm programming language focused on safety, performance, and concurrency. It is designed to be a "safe, concurrent, practical language", supporting functional and imperative-procedural paradigms. Rust's class API provides a way to create objects and classes in Rust.

Below is an example of a class in Rust:

```
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Point {
        Point { x, y }
    }

    fn origin() -> Point {
        Point { x: 0, y: 0 }
    }

    fn get_x(&self) -> i32 {
        self.x
    }

    fn get_y(&self) -> i32 {
        self.y
    }
}

fn main() {
    let point = Point::new(1, 2);
    println!("x = {}", point.get_x());
    println!("y = {}", point.get_y());
}
```
### Output
x = 1
y = 2

Explanation:
- `struct Point`: This defines a struct named Point which contains two fields, x and y, both of type i32.
- `impl Point`: This defines an implementation block for the Point struct. This is where methods for the Point struct are defined.
- `fn new(x: i32, y: i32) -> Point`: This defines a constructor method for the Point struct. It takes two parameters, x and y, both of type i32, and returns a Point object.
- `fn origin() -> Point`: This defines a static method for the Point struct. It returns a Point object with x and y set to 0.
- `fn get_x(&self) -> i32` and `fn get_y(&self) -> i32`: These define getter methods for the Point struct. They take a reference to the Point object as a parameter and return the value of the x and y fields, respectively.
- `let point = Point::new(1, 2)`: This creates a new Point object with x set to 1 and y set to 2.
- `println!("x = {}", point.get_x());` and `println!("y = {}", point.get_y());`: These print the values of the x and y fields of the Point object.

## Helpful links:
- https://doc.rust-lang.org/book/ch05-00-structs.html
- https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html