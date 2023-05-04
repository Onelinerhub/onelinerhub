# Rust struct with all public fields
// plain

A Rust struct with all public fields is a struct that has all of its fields declared as public. This means that any code outside of the struct can access and modify the fields.

## Example code

```rust
struct MyStruct {
    pub field1: i32,
    pub field2: String,
}

fn main() {
    let mut my_struct = MyStruct {
        field1: 10,
        field2: String::from("Hello"),
    };

    my_struct.field1 = 20;
    println!("field1 = {}", my_struct.field1);
}
```

## Output example

```
field1 = 20
```

## Code explanation

- `struct MyStruct {`: This is the start of the struct definition.
- `pub field1: i32,`: This declares a public field named `field1` of type `i32`.
- `pub field2: String,`: This declares a public field named `field2` of type `String`.
- `let mut my_struct = MyStruct {`: This creates a mutable instance of the `MyStruct` struct.
- `my_struct.field1 = 20;`: This assigns the value `20` to the `field1` field of the `my_struct` instance.
- `println!("field1 = {}", my_struct.field1);`: This prints the value of the `field1` field of the `my_struct` instance.

## Helpful links
- [Rust Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)

group: rust-struct