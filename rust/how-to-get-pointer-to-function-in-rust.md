# How to get pointer to function in Rust
// plain

In Rust, you can get a pointer to a function by using the `std::mem::transmute` function. This function takes a function pointer and returns a pointer to the function. To use this function, you must first create a function pointer type. For example, if you have a function `foo` that takes two `i32` parameters and returns an `i32`, you can create a function pointer type like this: `type FooFnPtr = fn(i32, i32) -> i32;`. Then you can use `std::mem::transmute` to get a pointer to the function like this: `let foo_ptr: *const FooFnPtr = std::mem::transmute(foo);`. The `foo_ptr` variable now holds a pointer to the `foo` function.

## Helpful links
- [std::mem::transmute](https://doc.rust-lang.org/std/mem/fn.transmute.html)
- [Function Pointers in Rust](https://doc.rust-lang.org/book/ch19-05-advanced-functions-and-closures.html#function-pointers)
- [Rust by Example - Function Pointers](https://doc.rust-lang.org/rust-by-example/fn/closures/fn_pointers.html)

group: rust-pointers