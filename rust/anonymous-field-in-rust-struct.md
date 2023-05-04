# Anonymous field in Rust struct
// plain

Anonymous fields in Rust structs are fields that do not have a name associated with them. They are declared using the `struct` keyword followed by the type of the field. For example:

```rust
struct Point {
    x: i32,
    y: i32,
    // Anonymous field
    i32,
}
```

The anonymous field in the above example is of type `i32`. It can be accessed using the `.` operator, just like any other field in the struct. For example:

```rust
let p = Point { x: 10, y: 20, 30 };
println!("{}", p.2); // Prints 30
```

## Code explanation


1. `struct Point {` - This is the start of the struct declaration.
2. `x: i32,` - This is a named field of type `i32`.
3. `y: i32,` - This is another named field of type `i32`.
4. `i32,` - This is the anonymous field of type `i32`.
5. `let p = Point { x: 10, y: 20, 30 };` - This is how an instance of the struct is created, with the anonymous field being set to `30`.
6. `println!("{}", p.2);` - This is how the anonymous field is accessed, using the `.` operator and the index of the field (in this case `2`).

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Anonymous Fields in Rust Structs](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#anonymous-fields-in-structs)

group: rust-struct