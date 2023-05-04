# How to init zero struct in Rust
// plain

In Rust, you can initialize a struct with all its fields set to zero using the `Default` trait. To do this, you must first implement the `Default` trait for the struct.

```rust
#[derive(Default)]
struct MyStruct {
    a: i32,
    b: i32,
    c: i32,
}

fn main() {
    let my_struct = MyStruct::default();
    println!("{:?}", my_struct);
}
```

## Output example

```
MyStruct { a: 0, b: 0, c: 0 }
```

## Code explanation

- `#[derive(Default)]`: This attribute is used to automatically implement the `Default` trait for the struct.
- `MyStruct::default()`: This is used to create an instance of the struct with all its fields set to zero.

## Helpful links
- [Rust Book - Default Trait](https://doc.rust-lang.org/book/ch10-02-traits.html#using-trait-bounds-to-conditionally-implement-methods)

group: rust-struct