# Example of struct private field in Rust
// plain

Struct private fields in Rust are fields that are not accessible outside of the struct. This can be controlled by using the `pub` keyword - use it to make public fields, while skip it for private ones.

## Example code

```rust
struct MyStruct {
    pub field1: i32,
    field2: i32,
}

fn main() {
    let my_struct = MyStruct {
        field1: 1,
        field2: 2,
    };

    println!("field1: {}", my_struct.field1);
    println!("field2: {}", my_struct.field2);
}
```

## Output example

```
field1: 1
field2: 2
```

## Code explanation

- `struct MyStruct {`: This is the start of the struct definition.
- `pub field1: i32,`: This is the first field of the struct, which is public and can be accessed outside of the struct.
- `field2: i32,`: This is the second field of the struct, which is private and cannot be accessed outside of the struct.
- `let my_struct = MyStruct {`: This is the start of the struct initialization.
- `field1: 1,`: This is the initialization of the first field of the struct.
- `field2: 2,`: This is the initialization of the second field of the struct.
- `println!("field1: {}", my_struct.field1);`: This is the print statement for the first field of the struct, which is public and can be accessed outside of the struct.
- `println!("field2: {}", my_struct.field2);`: This is the print statement for the second field of the struct, which is private and cannot be accessed outside of the struct.

## Helpful links
- [Rust Documentation - Structs](https://doc.rust-lang.org/book/ch05-00-structs.html)
- [Rust Documentation - Modules](https://doc.rust-lang.org/book/ch07-00-modules.html)

group: rust-struct
