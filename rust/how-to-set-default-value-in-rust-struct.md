# How to set default value in Rust struct
// plain

Setting a default value in a Rust struct is a simple process. To do this, you need to use the `Default` trait. This trait allows you to set a default value for a field in a struct.

## Example code

```rust
use std::default::Default;

#[derive(Default)]
struct MyStruct {
    field1: i32,
    field2: String,
}

fn main() {
    let my_struct = MyStruct::default();
    println!("{}", my_struct.field1);
    println!("{}", my_struct.field2);
}
```

## Output example

```
0

```

## Code explanation


1. `use std::default::Default;`: This imports the `Default` trait from the standard library.
2. `#[derive(Default)]`: This is a Rust attribute that tells the compiler to automatically implement the `Default` trait for the `MyStruct` struct.
3. `let my_struct = MyStruct::default();`: This creates an instance of `MyStruct` and sets the fields to their default values.
4. `println!("{}", my_struct.field1);`: This prints the value of `field1` which is set to 0 by the `Default` trait.
5. `println!("{}", my_struct.field2);`: This prints the value of `field2` which is set to an empty string by the `Default` trait.

## Helpful links

- [The Rust Programming Language - Default Trait](https://doc.rust-lang.org/std/default/trait.Default.html)
- [The Rust Programming Language - Derive Attribute](https://doc.rust-lang.org/reference/attributes/derive.html)

group: rust-struct