# Example of struct public field in Rust
// plain

A struct public field in Rust is a field of a struct that is accessible outside of the struct. This allows the struct to be used in a variety of ways, such as passing data between functions or creating a public API.

## Example code

```rust
struct MyStruct {
    pub field: i32,
}

fn main() {
    let my_struct = MyStruct { field: 5 };
    println!("{}", my_struct.field);
}
```

## Output example

```
5
```

## Code explanation


- `struct MyStruct {`: This line declares a new struct called `MyStruct`.
- `pub field: i32,`: This line declares a public field called `field` of type `i32`.
- `let my_struct = MyStruct { field: 5 };`: This line creates a new instance of `MyStruct` and assigns the value `5` to the `field` field.
- `println!("{}", my_struct.field);`: This line prints the value of the `field` field of the `my_struct` instance.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Public Fields](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#public-struct-fields)

group: rust-struct