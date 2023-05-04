# Rust struct of bytes example
// plain

A `struct` in Rust is a type of data structure that allows you to store multiple pieces of data in a single object. A `struct` of bytes is a type of `struct` that stores a sequence of bytes.

## Example code

```rust
struct Bytes {
    data: [u8; 8],
}

fn main() {
    let bytes = Bytes {
        data: [0, 1, 2, 3, 4, 5, 6, 7],
    };
    println!("{:?}", bytes);
}
```

## Output example

```
Bytes { data: [0, 1, 2, 3, 4, 5, 6, 7] }
```

## Code explanation


- `struct Bytes`: This is the definition of the `struct` of bytes. It contains a single field, `data`, which is an array of 8 `u8`s.
- `let bytes = Bytes { data: [0, 1, 2, 3, 4, 5, 6, 7], }`: This creates an instance of the `Bytes` `struct` with the given data.
- `println!("{:?}", bytes);`: This prints out the `Bytes` instance. The `{:?}` format specifier prints out the data in a debug format.

## Helpful links

- [Rust Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
- [Rust Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#scalar-types)
- [Rust Formatting](https://doc.rust-lang.org/std/fmt/)

group: rust-struct