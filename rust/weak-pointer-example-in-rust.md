# Weak pointer example in Rust
// plain

Weak pointers in Rust are used to access data without taking ownership of it. They are useful when you need to access data without preventing it from being dropped. A weak pointer is declared using the `Weak` type from the `std::rc` module. Here is an example of declaring a weak pointer:
```rust
use std::rc::Weak;

let weak_ptr: Weak<i32> = Weak::new();
```
The weak pointer is declared as a `Weak<i32>` type, which means it points to an `i32` type. The `Weak::new()` function is used to create a new weak pointer.

Output example:

No output is produced.

## Explanation

The `use std::rc::Weak` statement imports the `Weak` type from the `std::rc` module. This type is used to declare a weak pointer. The `Weak::new()` function is used to create a new weak pointer.

## Helpful links
- [Rust Documentation - Weak Pointers](https://doc.rust-lang.org/std/rc/struct.Weak.html)
- [Rust by Example - Weak Pointers](https://doc.rust-lang.org/rust-by-example/std_misc/weak.html)
- [Rust Book - Weak Pointers](https://doc.rust-lang.org/book/ch15-05-reference-counting.html#weak-references-and-cycles)

group: rust-pointers