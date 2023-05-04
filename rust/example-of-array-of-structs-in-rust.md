# Example of array of structs in Rust
// plain

An array of structs in Rust is a collection of structs stored in a contiguous memory location. Structs are custom data types that allow you to store multiple values of different types in a single variable. An array of structs is declared using the `[struct; size]` syntax, where `struct` is the struct type and `size` is the number of elements in the array.

## Example code

```rust
struct Point {
    x: i32,
    y: i32,
}

let points = [Point { x: 0, y: 0 }; 5];
```

## Output example

```
[
    Point { x: 0, y: 0 },
    Point { x: 0, y: 0 },
    Point { x: 0, y: 0 },
    Point { x: 0, y: 0 },
    Point { x: 0, y: 0 },
]
```

## Code explanation

- `struct Point { x: i32, y: i32, }`: This declares a struct type called `Point` with two fields, `x` and `y`, both of type `i32`.
- `let points = [Point { x: 0, y: 0 }; 5];`: This declares an array of `Point` structs with 5 elements, each with `x` and `y` fields set to `0`.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Arrays](https://doc.rust-lang.org/book/ch08-03-arrays.html)

group: rust-struct