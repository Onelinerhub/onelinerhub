# How to get struct fields in Rust
// plain

Structs in Rust are used to store data in a structured way. To access the fields of a struct, you can use the dot notation. For example:

```rust
struct Point {
    x: i32,
    y: i32,
}

let point = Point { x: 0, y: 0 };

println!("The x coordinate is {}", point.x);
```

## Output example

```
The x coordinate is 0
```

The code above creates a struct called `Point` with two fields, `x` and `y`. Then, it creates an instance of the `Point` struct and prints out the value of the `x` field.

You can also use the `let` keyword to destructure a struct and assign its fields to variables. For example:

```rust
let Point { x, y } = point;

println!("The x coordinate is {}", x);
```

## Output example

```
The x coordinate is 0
```

In the code above, the `let` keyword is used to destructure the `point` struct and assign its fields to the `x` and `y` variables. Then, the value of the `x` variable is printed out.

## Helpful links
- [Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Destructuring](https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#destructuring-to-break-apart-values)

group: rust-struct