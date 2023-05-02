# How to print pointer value in Rust
// plain

In Rust, you can print the value of a pointer by using the `*` operator. For example, if you have a pointer `ptr` pointing to a value `val`, you can print the value of `val` by using `println!("{}", *ptr);`. This will print the value of `val` that `ptr` is pointing to. Additionally, you can use the `format!` macro to format the output of the pointer value. For example, `println!("{:?}", *ptr);` will print the pointer value in a debug format. ## Helpful links [Rust Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html), [Rust Formatting](https://doc.rust-lang.org/std/fmt/index.html).

group: rust-pointers