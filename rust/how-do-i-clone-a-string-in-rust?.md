# How do I clone a string in Rust?
// plain

Cloning a string in Rust is a simple process. The `clone()` method can be used to create a deep copy of a string. The following example code creates a new string from an existing one:
```rust
let original_string = String::from("Hello World!");
let cloned_string = original_string.clone();
```
The `clone()` method creates a new string with the same contents as the original string. The new string is stored in the `cloned_string` variable.

## Code explanation


1. `let original_string = String::from("Hello World!");` - This line creates a new string with the contents "Hello World!" and stores it in the `original_string` variable.

2. `let cloned_string = original_string.clone();` - This line creates a deep copy of the `original_string` and stores it in the `cloned_string` variable.

## Helpful links

- [Clone trait](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Cloning a String](https://doc.rust-lang.org/book/ch15-03-cloning-objects.html#cloning-a-string)