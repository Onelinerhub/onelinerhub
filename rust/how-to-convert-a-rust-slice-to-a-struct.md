# How to convert a Rust slice to a struct?
// plain

To convert a Rust slice to a struct, you can use the `FromIterator` trait. This trait allows you to create a struct from an iterator of elements. For example:

```rust
use std::iter::FromIterator;

struct MyStruct {
    field1: i32,
    field2: i32,
}

let slice = &[1, 2];
let my_struct = MyStruct::from_iter(slice);

println!("{:?}", my_struct);
```

## Output example

```
MyStruct { field1: 1, field2: 2 }
```

## Code explanation

- `use std::iter::FromIterator;`: imports the `FromIterator` trait from the `std::iter` module.
- `struct MyStruct { field1: i32, field2: i32, }`: defines a struct with two fields of type `i32`.
- `let slice = &[1, 2];`: creates a slice containing two elements.
- `let my_struct = MyStruct::from_iter(slice);`: creates a `MyStruct` instance from the slice using the `FromIterator` trait.
- `println!("{:?}", my_struct);`: prints the `MyStruct` instance.

## Helpful links
- [Rust Documentation - FromIterator](https://doc.rust-lang.org/std/iter/trait.FromIterator.html)

group: rust-slice