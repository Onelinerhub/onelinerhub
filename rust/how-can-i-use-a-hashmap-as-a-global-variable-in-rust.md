# How can I use a hashmap as a global variable in Rust?
// plain

A global variable in Rust can be implemented using a `static` variable. A `static` variable is a variable that is stored in the program's read-only memory and is accessible from any part of the program.

A `static` variable can be used to store a `HashMap` as a global variable. The following example code creates a `static` variable `GLOBAL_MAP` that stores a `HashMap` with a `String` key and `i32` value:

```rust
static GLOBAL_MAP: HashMap<String, i32> = HashMap::new();
```

## Code explanation


- `static`: A keyword used to declare a static variable.
- `GLOBAL_MAP`: The name of the static variable.
- `HashMap<String, i32>`: The type of the static variable, a `HashMap` with a `String` key and `i32` value.
- `HashMap::new()`: A function that creates a new empty `HashMap`.

## Helpful links

- [Rust Book - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#differences-between-variables-and-constants)
- [Rust Book - HashMap](https://doc.rust-lang.org/book/ch08-03-hash-maps.html)

group: rust-variables